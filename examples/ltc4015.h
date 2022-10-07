#ifndef LTC4015_H_
#define LTC4015_H_

#include <stdint.h>


/* GENERATED_START: regs */
#define LTC4015_VBAT_LO_ALERT_LIMIT            0x01
#define LTC4015_VBAT_HI_ALERT_LIMIT            0x02
#define LTC4015_VIN_LO_ALERT_LIMIT             0x03
#define LTC4015_VIN_HI_ALERT_LIMIT             0x04
#define LTC4015_VSYS_LO_ALERT_LIMIT            0x05
#define LTC4015_VSYS_HI_ALERT_LIMIT            0x06
#define LTC4015_IIN_HI_ALERT_LIMIT             0x07
#define LTC4015_IBAT_LO_ALERT_LIMIT            0x08
#define LTC4015_DIE_TEMP_ALERT_LIMIT           0x09
#define LTC4015_BSR_HI_ALERT_LIMIT             0x0a
#define LTC4015_NTC_RATIO_HI_ALERT_LIMIT       0x0b
#define LTC4015_NTC_RATIO_LO_ALERT_LIMIT       0x0c
#define LTC4015_EN_LIMIT_ALERTS                0x0d
#define LTC4015_EN_CHARGER_STATE_ALERTS        0x0e
#define LTC4015_EN_CHARGE_STATUS_ALERTS        0x0f
#define LTC4015_QCOUNT_LO_ALERT_LIMIT          0x10
#define LTC4015_QCOUNT_HI_ALERT_LIMIT          0x11
#define LTC4015_QCOUNT_PRESCALE_FACTOR         0x12
#define LTC4015_QCOUNT                         0x13
#define LTC4015_CONFIG_BITS                    0x14
#define LTC4015_IIN_LIMIT_SETTING              0x15
#define LTC4015_VIN_UVCL_SETTING               0x16
#define LTC4015_ARM_SHIP_MODE                  0x19
#define LTC4015_ICHARGE_TARGET                 0x1a
#define LTC4015_VCHARGE_TARGET                 0x1b
#define LTC4015_C_OVER_X_THRESHOLD             0x1c
#define LTC4015_MAX_CV_TIME                    0x1d
#define LTC4015_MAX_CHARGE_TIME                0x1e
#define LTC4015_JEITA_T1                       0x1f
#define LTC4015_JEITA_T2                       0x20
#define LTC4015_JEITA_T3                       0x21
#define LTC4015_JEITA_T4                       0x22
#define LTC4015_JEITA_T5                       0x23
#define LTC4015_JEITA_T6                       0x24
#define LTC4015_VCHARGE_JEITA_6_5              0x25
#define LTC4015_VCHARGE_JEITA_4_3_2            0x26
#define LTC4015_ICHARGE_JEITA_6_5              0x27
#define LTC4015_ICHARGE_JEITA_4_3_2            0x28
#define LTC4015_CHARGER_CONFIG_BITS            0x29
#define LTC4015_VABSORB_DELTA                  0x2a
#define LTC4015_MAX_ABSORB_TIME                0x2b
#define LTC4015_VEQUALIZE_DELTA                0x2c
#define LTC4015_EQUALIZE_TIME                  0x2d
#define LTC4015_LIFEPO4_RECHARGE_THRESHOLD     0x2e
#define LTC4015_MAX_CHARGE_TIMER               0x30
#define LTC4015_CV_TIMER                       0x31
#define LTC4015_ABSORB_TIMER                   0x32
#define LTC4015_EQUALIZE_TIMER                 0x33
#define LTC4015_CHARGE_STATE                   0x34
#define LTC4015_CHARGE_STATUS                  0x35
#define LTC4015_LIMIT_ALERTS                   0x36
#define LTC4015_CHARGER_STATE_ALERTS           0x37
#define LTC4015_CHARGER_STATUS_ALERTS          0x38
#define LTC4015_SYSTEM_STATUS                  0x39
#define LTC4015_VBAT                           0x3a
#define LTC4015_VIN                            0x3b
#define LTC4015_VSYS                           0x3c
#define LTC4015_IBAT                           0x3d
#define LTC4015_IIN                            0x3e
#define LTC4015_DIE_TEMP                       0x3f
#define LTC4015_NTC_RATIO                      0x40
#define LTC4015_BSR                            0x41
#define LTC4015_JEITA_REGION                   0x42
#define LTC4015_CHEM_CELLS                     0x43
#define LTC4015_ICHARGE_DAC                    0x44
#define LTC4015_VCHARGE_DAC                    0x45
#define LTC4015_IIN_LIMIT_DAC                  0x46
#define LTC4015_VBAT_FILT                      0x47
#define LTC4015_ICHARGE_BSR                    0x48
#define LTC4015_MEAS_SYS_VALID                 0x4a/* GENERATED_END */

/* GENERATED_START: typedefs */

typedef union {
    struct {
        uint8_t en_ntc_ratio_lo_alert : 1;
        uint8_t en_ntc_ratio_hi_alert : 1;
        uint8_t en_bsr_hi_alert : 1;
        uint8_t en_die_temp_hi_alert : 1;
        uint8_t en_ibat_lo_alert : 1;
        uint8_t en_iin_hi_alert : 1;
        uint8_t en_vsys_hi_alert : 1;
        uint8_t en_vsys_lo_alert : 1;
        uint8_t en_vin_hi_alert : 1;
        uint8_t en_vin_lo_alert : 1;
        uint8_t en_vbat_hi_alert : 1;
        uint8_t en_vbat_lo_alert : 1;
        uint8_t en_qcount_hi_alert : 1;
        uint8_t en_qcount_low_alert : 1;
        uint8_t reserved_0 : 1;
        uint8_t en_meas_sys_valid_alert : 1;
    } fields;
    uint16_t bits;
} LTC4015_EN_LIMIT_ALERTS_TypeDef;

typedef union {
    struct {
        uint8_t en_bat_short_fault_alert : 1;
        uint8_t en_bat_missing_fault_alert : 1;
        uint8_t en_max_charge_time_fault_alert : 1;
        uint8_t en_c_over_x_term_alert : 1;
        uint8_t en_timer_term_alert : 1;
        uint8_t en_ntc_pause_alert : 1;
        uint8_t en_cc_cv_charge_alert : 1;
        uint8_t en_precharge_alert : 1;
        uint8_t en_charger_suspended_alert : 1;
        uint8_t en_absorb_charge_alert : 1;
        uint8_t en_equalize_charge_alert : 1;
    } fields;
    uint16_t bits;
} LTC4015_EN_CHARGER_STATE_ALERTS_TypeDef;

typedef union {
    struct {
        uint8_t en_constant_voltage_alert : 1;
        uint8_t en_constatn_current_alert : 1;
        uint8_t en_iin_limit_active_alert : 1;
        uint8_t en_vin_uvlc_active_alert : 1;
    } fields;
    uint16_t bits;
} LTC4015_EN_CHARGE_STATUS_ALERTS_TypeDef;

typedef union {
    struct {
        uint8_t reserved_0 : 2;
        uint8_t en_qcount : 1;
        uint8_t mppt_en_i2c : 1;
        uint8_t force_meas_sys_on : 1;
        uint8_t run_brs : 1;
        uint8_t reserved_1 : 2;
        uint8_t suspend_charger : 1;
    } fields;
    uint16_t bits;
} LTC4015_CONFIG_BITS_TypeDef;

typedef union {
    struct {
        uint8_t vcharge_jeita_5 : 5;
        uint8_t vcharge_jeita_6 : 5;
    } fields;
    uint16_t bits;
} LTC4015_VCHARGE_JEITA_6_5_TypeDef;

typedef union {
    struct {
        uint8_t vcharge_jeita_2 : 5;
        uint8_t vcharge_jeita_3 : 5;
        uint8_t vcharge_jeita_4 : 5;
    } fields;
    uint16_t bits;
} LTC4015_VCHARGE_JEITA_4_3_2_TypeDef;

typedef union {
    struct {
        uint8_t icharge_jeita_5 : 5;
        uint8_t icharge_jeita_6 : 5;
    } fields;
    uint16_t bits;
} LTC4015_ICHARGE_JEITA_6_5_TypeDef;

typedef union {
    struct {
        uint8_t icharge_jeita_2 : 5;
        uint8_t icharge_jeita_3 : 5;
        uint8_t icharge_jeita_4 : 5;
    } fields;
    uint16_t bits;
} LTC4015_ICHARGE_JEITA_4_3_2_TypeDef;

typedef union {
    struct {
        uint8_t en_jeita : 1;
        uint8_t en_lead_acid_temp_comp : 1;
        uint8_t en_c_over_x_term : 1;
    } fields;
    uint16_t bits;
} LTC4015_CHARGER_CONFIG_BITS_TypeDef;

typedef union {
    struct {
        uint8_t bat_short_fault : 1;
        uint8_t bat_missing_fault : 1;
        uint8_t max_charge_time_fault : 1;
        uint8_t c_over_x_term : 1;
        uint8_t timer_term : 1;
        uint8_t ntc_pause : 1;
        uint8_t cc_cv_charge : 1;
        uint8_t precharge : 1;
        uint8_t charger_suspended : 1;
        uint8_t absorb_charge : 1;
        uint8_t equalize_charge : 1;
    } fields;
    uint16_t bits;
} LTC4015_CHARGE_STATE_TypeDef;

typedef union {
    struct {
        uint8_t constatn_voltage : 1;
        uint8_t constnt_current : 1;
        uint8_t iin_limit_active : 1;
        uint8_t vin_uvcl_active : 1;
    } fields;
    uint16_t bits;
} LTC4015_CHARGE_STATUS_TypeDef;

typedef union {
    struct {
        uint8_t ntc_ratio_lo_alert : 1;
        uint8_t ntc_ratio_hi_alert : 1;
        uint8_t bst_hi_alert : 1;
        uint8_t die_temp_hi_alert : 1;
        uint8_t ibat_lo_alert : 1;
        uint8_t iin_hi_alert : 1;
        uint8_t vsys_hi_alert : 1;
        uint8_t vsys_lo_alert : 1;
        uint8_t vin_hi_alert : 1;
        uint8_t vin_lo_alert : 1;
        uint8_t vbat_hi_alert : 1;
        uint8_t vbat_lo_alert : 1;
        uint8_t qcount_hi_alert : 1;
        uint8_t qcount_lo_alert : 1;
        uint8_t reserved_0 : 1;
        uint8_t meas_sys_valid_alert : 1;
    } fields;
    uint16_t bits;
} LTC4015_LIMIT_ALERTS_TypeDef;

typedef union {
    struct {
        uint8_t bat_short_fault_alert : 1;
        uint8_t bat_missing_fault_alert : 1;
        uint8_t max_charge_time_fault_alert : 1;
        uint8_t c_over_x_term_alert : 1;
        uint8_t timer_term_alert : 1;
        uint8_t ntc_pause_alert : 1;
        uint8_t cc_cv_charge_alert : 1;
        uint8_t precharge_alert : 1;
        uint8_t charger_suspended_alert : 1;
        uint8_t absorb_charge_alert : 1;
        uint8_t equalize_charge_alert : 1;
    } fields;
    uint16_t bits;
} LTC4015_CHARGER_STATE_ALERTS_TypeDef;

typedef union {
    struct {
        uint8_t constatn_voltage_alert : 1;
        uint8_t constant_current_alert : 1;
        uint8_t iin_limit_active_alert : 1;
        uint8_t vin_uvcl_active_alert : 1;
    } fields;
    uint16_t bits;
} LTC4015_CHARGER_STATUS_ALERTS_TypeDef;

typedef union {
    struct {
        uint8_t intvcc_gt_2p8v : 1;
        uint8_t intvcc_gt_4p3v : 1;
        uint8_t vin_gt_bat : 1;
        uint8_t vin_ovlo : 1;
        uint8_t thermal_shutdown : 1;
        uint8_t no_rt : 1;
        uint8_t ok_to_charge : 1;
        uint8_t reserved_0 : 1;
        uint8_t cell_count_error : 1;
        uint8_t drvcc_good : 1;
        uint8_t equalize_req : 1;
        uint8_t mppt_en_pin : 1;
        uint8_t reserved_1 : 1;
        uint8_t charge_enabled : 1;
    } fields;
    uint16_t bits;
} LTC4015_SYSTEM_STATUS_TypeDef;

typedef union {
    struct {
        uint8_t cell_count_pins : 4;
        uint8_t reserved_0 : 4;
        uint8_t chem : 4;
    } fields;
    uint16_t bits;
} LTC4015_CHEM_CELLS_TypeDef;
/* GENERATED_END */
/* GENERATED_START: print */

void LTC4015_print_EN_LIMIT_ALERTS(LTC4015_EN_LIMIT_ALERTS_TypeDef reg) {
    printf("EN_LIMIT_ALERTS = 0x%04x\n", reg);
    printf(" .en_meas_sys_valid_alert = %d\n", reg.fields.en_meas_sys_valid_alert);
    printf(" .en_qcount_low_alert = %d\n", reg.fields.en_qcount_low_alert);
    printf(" .en_qcount_hi_alert = %d\n", reg.fields.en_qcount_hi_alert);
    printf(" .en_vbat_lo_alert = %d\n", reg.fields.en_vbat_lo_alert);
    printf(" .en_vbat_hi_alert = %d\n", reg.fields.en_vbat_hi_alert);
    printf(" .en_vin_lo_alert = %d\n", reg.fields.en_vin_lo_alert);
    printf(" .en_vin_hi_alert = %d\n", reg.fields.en_vin_hi_alert);
    printf(" .en_vsys_lo_alert = %d\n", reg.fields.en_vsys_lo_alert);
    printf(" .en_vsys_hi_alert = %d\n", reg.fields.en_vsys_hi_alert);
    printf(" .en_iin_hi_alert = %d\n", reg.fields.en_iin_hi_alert);
    printf(" .en_ibat_lo_alert = %d\n", reg.fields.en_ibat_lo_alert);
    printf(" .en_die_temp_hi_alert = %d\n", reg.fields.en_die_temp_hi_alert);
    printf(" .en_bsr_hi_alert = %d\n", reg.fields.en_bsr_hi_alert);
    printf(" .en_ntc_ratio_hi_alert = %d\n", reg.fields.en_ntc_ratio_hi_alert);
    printf(" .en_ntc_ratio_lo_alert = %d\n", reg.fields.en_ntc_ratio_lo_alert);
}

void LTC4015_print_EN_CHARGER_STATE_ALERTS(LTC4015_EN_CHARGER_STATE_ALERTS_TypeDef reg) {
    printf("EN_CHARGER_STATE_ALERTS = 0x%04x\n", reg);
    printf(" .en_equalize_charge_alert = %d\n", reg.fields.en_equalize_charge_alert);
    printf(" .en_absorb_charge_alert = %d\n", reg.fields.en_absorb_charge_alert);
    printf(" .en_charger_suspended_alert = %d\n", reg.fields.en_charger_suspended_alert);
    printf(" .en_precharge_alert = %d\n", reg.fields.en_precharge_alert);
    printf(" .en_cc_cv_charge_alert = %d\n", reg.fields.en_cc_cv_charge_alert);
    printf(" .en_ntc_pause_alert = %d\n", reg.fields.en_ntc_pause_alert);
    printf(" .en_timer_term_alert = %d\n", reg.fields.en_timer_term_alert);
    printf(" .en_c_over_x_term_alert = %d\n", reg.fields.en_c_over_x_term_alert);
    printf(" .en_max_charge_time_fault_alert = %d\n", reg.fields.en_max_charge_time_fault_alert);
    printf(" .en_bat_missing_fault_alert = %d\n", reg.fields.en_bat_missing_fault_alert);
    printf(" .en_bat_short_fault_alert = %d\n", reg.fields.en_bat_short_fault_alert);
}

void LTC4015_print_EN_CHARGE_STATUS_ALERTS(LTC4015_EN_CHARGE_STATUS_ALERTS_TypeDef reg) {
    printf("EN_CHARGE_STATUS_ALERTS = 0x%04x\n", reg);
    printf(" .en_vin_uvlc_active_alert = %d\n", reg.fields.en_vin_uvlc_active_alert);
    printf(" .en_iin_limit_active_alert = %d\n", reg.fields.en_iin_limit_active_alert);
    printf(" .en_constatn_current_alert = %d\n", reg.fields.en_constatn_current_alert);
    printf(" .en_constant_voltage_alert = %d\n", reg.fields.en_constant_voltage_alert);
}

void LTC4015_print_CONFIG_BITS(LTC4015_CONFIG_BITS_TypeDef reg) {
    printf("CONFIG_BITS = 0x%04x\n", reg);
    printf(" .suspend_charger = %d\n", reg.fields.suspend_charger);
    printf(" .run_brs = %d\n", reg.fields.run_brs);
    printf(" .force_meas_sys_on = %d\n", reg.fields.force_meas_sys_on);
    printf(" .mppt_en_i2c = %d\n", reg.fields.mppt_en_i2c);
    printf(" .en_qcount = %d\n", reg.fields.en_qcount);
}

void LTC4015_print_VCHARGE_JEITA_6_5(LTC4015_VCHARGE_JEITA_6_5_TypeDef reg) {
    printf("VCHARGE_JEITA_6_5 = 0x%04x\n", reg);
    printf(" .vcharge_jeita_6 = 0x%04x\n", reg.fields.vcharge_jeita_6);
    printf(" .vcharge_jeita_5 = 0x%04x\n", reg.fields.vcharge_jeita_5);
}

void LTC4015_print_VCHARGE_JEITA_4_3_2(LTC4015_VCHARGE_JEITA_4_3_2_TypeDef reg) {
    printf("VCHARGE_JEITA_4_3_2 = 0x%04x\n", reg);
    printf(" .vcharge_jeita_4 = 0x%04x\n", reg.fields.vcharge_jeita_4);
    printf(" .vcharge_jeita_3 = 0x%04x\n", reg.fields.vcharge_jeita_3);
    printf(" .vcharge_jeita_2 = 0x%04x\n", reg.fields.vcharge_jeita_2);
}

void LTC4015_print_ICHARGE_JEITA_6_5(LTC4015_ICHARGE_JEITA_6_5_TypeDef reg) {
    printf("ICHARGE_JEITA_6_5 = 0x%04x\n", reg);
    printf(" .icharge_jeita_6 = 0x%04x\n", reg.fields.icharge_jeita_6);
    printf(" .icharge_jeita_5 = 0x%04x\n", reg.fields.icharge_jeita_5);
}

void LTC4015_print_ICHARGE_JEITA_4_3_2(LTC4015_ICHARGE_JEITA_4_3_2_TypeDef reg) {
    printf("ICHARGE_JEITA_4_3_2 = 0x%04x\n", reg);
    printf(" .icharge_jeita_4 = 0x%04x\n", reg.fields.icharge_jeita_4);
    printf(" .icharge_jeita_3 = 0x%04x\n", reg.fields.icharge_jeita_3);
    printf(" .icharge_jeita_2 = 0x%04x\n", reg.fields.icharge_jeita_2);
}

void LTC4015_print_CHARGER_CONFIG_BITS(LTC4015_CHARGER_CONFIG_BITS_TypeDef reg) {
    printf("CHARGER_CONFIG_BITS = 0x%04x\n", reg);
    printf(" .en_c_over_x_term = %d\n", reg.fields.en_c_over_x_term);
    printf(" .en_lead_acid_temp_comp = %d\n", reg.fields.en_lead_acid_temp_comp);
    printf(" .en_jeita = %d\n", reg.fields.en_jeita);
}

void LTC4015_print_CHARGE_STATE(LTC4015_CHARGE_STATE_TypeDef reg) {
    printf("CHARGE_STATE = 0x%04x\n", reg);
    printf(" .equalize_charge = %d\n", reg.fields.equalize_charge);
    printf(" .absorb_charge = %d\n", reg.fields.absorb_charge);
    printf(" .charger_suspended = %d\n", reg.fields.charger_suspended);
    printf(" .precharge = %d\n", reg.fields.precharge);
    printf(" .cc_cv_charge = %d\n", reg.fields.cc_cv_charge);
    printf(" .ntc_pause = %d\n", reg.fields.ntc_pause);
    printf(" .timer_term = %d\n", reg.fields.timer_term);
    printf(" .c_over_x_term = %d\n", reg.fields.c_over_x_term);
    printf(" .max_charge_time_fault = %d\n", reg.fields.max_charge_time_fault);
    printf(" .bat_missing_fault = %d\n", reg.fields.bat_missing_fault);
    printf(" .bat_short_fault = %d\n", reg.fields.bat_short_fault);
}

void LTC4015_print_CHARGE_STATUS(LTC4015_CHARGE_STATUS_TypeDef reg) {
    printf("CHARGE_STATUS = 0x%04x\n", reg);
    printf(" .vin_uvcl_active = %d\n", reg.fields.vin_uvcl_active);
    printf(" .iin_limit_active = %d\n", reg.fields.iin_limit_active);
    printf(" .constnt_current = %d\n", reg.fields.constnt_current);
    printf(" .constatn_voltage = %d\n", reg.fields.constatn_voltage);
}

void LTC4015_print_LIMIT_ALERTS(LTC4015_LIMIT_ALERTS_TypeDef reg) {
    printf("LIMIT_ALERTS = 0x%04x\n", reg);
    printf(" .meas_sys_valid_alert = %d\n", reg.fields.meas_sys_valid_alert);
    printf(" .qcount_lo_alert = %d\n", reg.fields.qcount_lo_alert);
    printf(" .qcount_hi_alert = %d\n", reg.fields.qcount_hi_alert);
    printf(" .vbat_lo_alert = %d\n", reg.fields.vbat_lo_alert);
    printf(" .vbat_hi_alert = %d\n", reg.fields.vbat_hi_alert);
    printf(" .vin_lo_alert = %d\n", reg.fields.vin_lo_alert);
    printf(" .vin_hi_alert = %d\n", reg.fields.vin_hi_alert);
    printf(" .vsys_lo_alert = %d\n", reg.fields.vsys_lo_alert);
    printf(" .vsys_hi_alert = %d\n", reg.fields.vsys_hi_alert);
    printf(" .iin_hi_alert = %d\n", reg.fields.iin_hi_alert);
    printf(" .ibat_lo_alert = %d\n", reg.fields.ibat_lo_alert);
    printf(" .die_temp_hi_alert = %d\n", reg.fields.die_temp_hi_alert);
    printf(" .bst_hi_alert = %d\n", reg.fields.bst_hi_alert);
    printf(" .ntc_ratio_hi_alert = %d\n", reg.fields.ntc_ratio_hi_alert);
    printf(" .ntc_ratio_lo_alert = %d\n", reg.fields.ntc_ratio_lo_alert);
}

void LTC4015_print_CHARGER_STATE_ALERTS(LTC4015_CHARGER_STATE_ALERTS_TypeDef reg) {
    printf("CHARGER_STATE_ALERTS = 0x%04x\n", reg);
    printf(" .equalize_charge_alert = %d\n", reg.fields.equalize_charge_alert);
    printf(" .absorb_charge_alert = %d\n", reg.fields.absorb_charge_alert);
    printf(" .charger_suspended_alert = %d\n", reg.fields.charger_suspended_alert);
    printf(" .precharge_alert = %d\n", reg.fields.precharge_alert);
    printf(" .cc_cv_charge_alert = %d\n", reg.fields.cc_cv_charge_alert);
    printf(" .ntc_pause_alert = %d\n", reg.fields.ntc_pause_alert);
    printf(" .timer_term_alert = %d\n", reg.fields.timer_term_alert);
    printf(" .c_over_x_term_alert = %d\n", reg.fields.c_over_x_term_alert);
    printf(" .max_charge_time_fault_alert = %d\n", reg.fields.max_charge_time_fault_alert);
    printf(" .bat_missing_fault_alert = %d\n", reg.fields.bat_missing_fault_alert);
    printf(" .bat_short_fault_alert = %d\n", reg.fields.bat_short_fault_alert);
}

void LTC4015_print_CHARGER_STATUS_ALERTS(LTC4015_CHARGER_STATUS_ALERTS_TypeDef reg) {
    printf("CHARGER_STATUS_ALERTS = 0x%04x\n", reg);
    printf(" .vin_uvcl_active_alert = %d\n", reg.fields.vin_uvcl_active_alert);
    printf(" .iin_limit_active_alert = %d\n", reg.fields.iin_limit_active_alert);
    printf(" .constant_current_alert = %d\n", reg.fields.constant_current_alert);
    printf(" .constatn_voltage_alert = %d\n", reg.fields.constatn_voltage_alert);
}

void LTC4015_print_SYSTEM_STATUS(LTC4015_SYSTEM_STATUS_TypeDef reg) {
    printf("SYSTEM_STATUS = 0x%04x\n", reg);
    printf(" .charge_enabled = %d\n", reg.fields.charge_enabled);
    printf(" .mppt_en_pin = %d\n", reg.fields.mppt_en_pin);
    printf(" .equalize_req = %d\n", reg.fields.equalize_req);
    printf(" .drvcc_good = %d\n", reg.fields.drvcc_good);
    printf(" .cell_count_error = %d\n", reg.fields.cell_count_error);
    printf(" .ok_to_charge = %d\n", reg.fields.ok_to_charge);
    printf(" .no_rt = %d\n", reg.fields.no_rt);
    printf(" .thermal_shutdown = %d\n", reg.fields.thermal_shutdown);
    printf(" .vin_ovlo = %d\n", reg.fields.vin_ovlo);
    printf(" .vin_gt_bat = %d\n", reg.fields.vin_gt_bat);
    printf(" .intvcc_gt_4p3v = %d\n", reg.fields.intvcc_gt_4p3v);
    printf(" .intvcc_gt_2p8v = %d\n", reg.fields.intvcc_gt_2p8v);
}

void LTC4015_print_CHEM_CELLS(LTC4015_CHEM_CELLS_TypeDef reg) {
    printf("CHEM_CELLS = 0x%04x\n", reg);
    printf(" .chem = 0x%04x\n", reg.fields.chem);
    printf(" .cell_count_pins = 0x%04x\n", reg.fields.cell_count_pins);
}
/* GENERATED_END */


#endif /* ifndef LTC4015_H_ */
