from rdl import Register
from rdl.devices import ltc4015
from rdl.output import Output


out = Output("ltc4015.h")

# Register address definitions
lines = []
for reg in ltc4015.get_all(cls=Register):
    lines.append(f"#define LTC4015_{reg.name:30s} 0x{reg.address:02x}")
text = '\n'.join(lines)
out.replace_section("regs", text)

# Register typedefs

from jinja2 import Template

typedef_tpl = Template("""
typedef union {
    struct {
{%- for field in fields %}
        uint8_t {{field[0]}} : {{field[1]}};
{%- endfor %}
    } fields;
    uint16_t bits;
} LTC4015_{{name}}_TypeDef;
""")

text = ""

for reg in ltc4015.get_all(cls=Register):
    if len(reg.fields) > 1:
        last_start = 0
        reserved_counter = 0
        param = dict()
        param['name'] = reg.name
        param['fields'] = []
        for field in reg.get_sorted_fields():


            space = field.lsb - last_start
            if space > 0:
                param['fields'].append((f"reserved_{reserved_counter}", space))
                reserved_counter += 1

            param['fields'].append((field.name, field.size))
            last_start = field.msb + 1

        text += typedef_tpl.render(**param)
        text += '\n'

out.replace_section("typedefs", text)

#%% Print

text = ""

typedef_tpl = Template("""
void LTC4015_print_{{name}}(LTC4015_{{name}}_TypeDef reg) {
    printf("{{name}} = 0x%04x\\n", reg);
{%- for field in fields %}
    {%- if field.size == 1 %}
    printf(" .{{field.name}} = %d\\n", reg.fields.{{field.name}});
    {%- else %}
    printf(" .{{field.name}} = 0x%04x\\n", reg.fields.{{field.name}});
    {%- endif %}
{%- endfor %}
}
""")

for reg in ltc4015.get_all(cls=Register):
    if len(reg.fields) > 1:
        last_start = 0
        reserved_counter = 0
        param = dict()
        param['name'] = reg.name
        param['fields'] = reversed(reg.get_sorted_fields());


        text += typedef_tpl.render(**param)
        text += "\n"

out.replace_section("print", text)

# Write output
out.write()
