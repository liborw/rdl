
from rdl import Register, Field

defs = {'asize_b': 8, 'dsize_b': 16}

regs = [
    Register(0x01, value=0, name='VBAT_LO_ALERT_LIMIT', **defs),
    Register(0x02, value=0, name='VBAT_HI_ALERT_LIMIT', **defs),
    Register(0x03, value=0, name='VIN_LO_ALERT_LIMIT', **defs),
    Register(0x04, value=0, name='VIN_HI_ALERT_LIMIT', **defs),
    Register(0x05, value=0, name='VSYS_LO_ALERT_LIMIT', **defs),
    Register(0x06, value=0, name='VSYS_HI_ALERT_LIMIT', **defs),
    Register(0x07, value=0, name='IIN_HI_ALERT_LIMIT', **defs),
    Register(0x08, value=0, name='IBAT_LO_ALERT_LIMIT', **defs),
    Register(0x09, value=0, name='DIE_TEMP_ALERT_LIMIT', **defs),
    Register(0x0a, value=0, name='BSR_HI_ALERT_LIMIT', **defs),
    Register(0x0b, value=0, name='NTC_RATIO_HI_ALERT_LIMIT', **defs),
    Register(0x0c, value=0, name='NTC_RATIO_LO_ALERT_LIMIT', **defs),
    Register(0x0d, value=0, name='EN_LIMIT_ALERTS', **defs, fields=[
        Field('en_meas_sys_valid_alert', 15),
        Field('en_qcount_low_alert', 13),
        Field('en_qcount_hi_alert', 12),
        Field('en_vbat_lo_alert', 11),
        Field('en_vbat_hi_alert', 10),
        Field('en_vin_lo_alert', 9),
        Field('en_vin_hi_alert', 8),
        Field('en_vsys_lo_alert', 7),
        Field('en_vsys_hi_alert', 6),
        Field('en_iin_hi_alert', 5),
        Field('en_ibat_lo_alert', 4),
        Field('en_die_temp_hi_alert', 3),
        Field('en_bsr_hi_alert', 2),
        Field('en_ntc_ratio_hi_alert', 1),
        Field('en_ntc_ratio_lo_alert', 0)]),
    Register(0x0e, value=0, name='EN_CHARGER_STATE_ALERTS', **defs, fields=[
        Field('en_equalize_charge_alert', 10),
        Field('en_absorb_charge_alert', 9),
        Field('en_charger_suspended_alert', 8),
        Field('en_precharge_alert', 7),
        Field('en_cc_cv_charge_alert', 6),
        Field('en_ntc_pause_alert', 5),
        Field('en_timer_term_alert', 4),
        Field('en_c_over_x_term_alert', 3),
        Field('en_max_charge_time_fault_alert', 2),
        Field('en_bat_missing_fault_alert', 1),
        Field('en_bat_short_fault_alert', 0)]),
    Register(0x0f, value=0, name='EN_CHARGE_STATUS_ALERTS', **defs, fields=[
        Field('en_vin_uvlc_active_alert', 3),
        Field('en_iin_limit_active_alert', 2),
        Field('en_constatn_current_alert', 1),
        Field('en_constant_voltage_alert', 0)]),
    Register(0x10, value=0, name='QCOUNT_LO_ALERT_LIMIT', **defs),
    Register(0x11, value=0, name='QCOUNT_HI_ALERT_LIMIT', **defs),
    Register(0x12, value=0, name='QCOUNT_PRESCALE_FACTOR', **defs),
    Register(0x13, value=0, name='QCOUNT', **defs),
    Register(0x14, value=0, name='CONFIG_BITS', **defs, fields=[
        Field('suspend_charger', 8),
        Field('run_brs', 5),
        Field('force_meas_sys_on', 4),
        Field('mppt_en_i2c', 3),
        Field('en_qcount', 2)]),
    Register(0x15, value=0x3f, name='IIN_LIMIT_SETTING', **defs, fields=[
        Field('iin_limit_setting', 5, 0)]),
    Register(0x16, value=0xff, name='VIN_UVCL_SETTING', **defs, fields=[
        Field('vin_uvcl_settings', 7, 0)]),
    Register(0x19, value=0, name='ARM_SHIP_MODE', **defs),
    Register(0x1a, value=0, name='ICHARGE_TARGET', **defs, fields=[
        Field('icharge_target', 4, 0)]),
    Register(0x1b, value=0, name='VCHARGE_TARGET', **defs, fields=[
        Field('vcharge_target', 5, 0)]),
    Register(0x1c, value=0, name='C_OVER_X_THRESHOLD', **defs),
    Register(0x1d, value=0, name='MAX_CV_TIME', **defs),
    Register(0x1e, value=0, name='MAX_CHARGE_TIME', **defs),
    Register(0x1f, value=0x3f00, name='JEITA_T1', **defs),
    Register(0x20, value=0x372a, name='JEITA_T2', **defs),
    Register(0x21, value=0x1f27, name='JEITA_T3', **defs),
    Register(0x22, value=0x1bcc, name='JEITA_T4', **defs),
    Register(0x23, value=0x18b9, name='JEITA_T5', **defs),
    Register(0x24, value=0x136d, name='JEITA_T6', **defs),
    Register(0x25, value=0, name='VCHARGE_JEITA_6_5', **defs, fields=[
        Field('vcharge_jeita_6', 9, 5),
        Field('vcharge_jeita_5', 4, 0)]),
    Register(0x26, value=0, name='VCHARGE_JEITA_4_3_2', **defs, fields=[
        Field('vcharge_jeita_4', 14, 10),
        Field('vcharge_jeita_3', 9, 5),
        Field('vcharge_jeita_2', 4, 0)]),
    Register(0x27, value=0x01ef, name='ICHARGE_JEITA_6_5', **defs, fields=[
        Field('icharge_jeita_6', 9, 5),
        Field('icharge_jeita_5', 4, 0)]),
    Register(0x28, value=0x7fef, name='ICHARGE_JEITA_4_3_2', **defs, fields=[
        Field('icharge_jeita_4', 14, 10),
        Field('icharge_jeita_3', 9, 5),
        Field('icharge_jeita_2', 4, 0)]),
    Register(0x29, value=0, name='CHARGER_CONFIG_BITS', **defs, fields=[
        Field('en_c_over_x_term', 2),
        Field('en_lead_acid_temp_comp', 1),
        Field('en_jeita', 0)]),
    Register(0x2a, value=0, name='VABSORB_DELTA', **defs, fields=[
        Field('vabsorb_delta', 5, 0)]),
    Register(0x2b, value=0, name='MAX_ABSORB_TIME', **defs),
    Register(0x2c, value=0x002a, name='VEQUALIZE_DELTA', **defs, fields=[
        Field('vequalize_delta', 5, 0)]),
    Register(0x2d, value=0x0e10, name='EQUALIZE_TIME', **defs),
    Register(0x2e, value=0x4410, name='LIFEPO4_RECHARGE_THRESHOLD', **defs),
    Register(0x30, value=0, name='MAX_CHARGE_TIMER', **defs),
    Register(0x31, value=0, name='CV_TIMER', **defs),
    Register(0x32, value=0, name='ABSORB_TIMER', **defs),
    Register(0x33, value=0, name='EQUALIZE_TIMER', **defs),
    Register(0x34, value=0, name='CHARGE_STATE', **defs, fields=[
        Field('equalize_charge', 10),
        Field('absorb_charge', 9),
        Field('charger_suspended', 8),
        Field('precharge', 7),
        Field('cc_cv_charge', 6),
        Field('ntc_pause', 5),
        Field('timer_term', 4),
        Field('c_over_x_term', 3),
        Field('max_charge_time_fault', 2),
        Field('bat_missing_fault', 1),
        Field('bat_short_fault', 0)]),
    Register(0x35, value=0, name='CHARGE_STATUS', **defs, fields=[
        Field('vin_uvcl_active', 3),
        Field('iin_limit_active', 2),
        Field('constnt_current', 1),
        Field('constatn_voltage', 0)]),
    Register(0x36, value=0, name='LIMIT_ALERTS', **defs, fields=[
        Field('meas_sys_valid_alert', 15),
        Field('qcount_lo_alert', 13),
        Field('qcount_hi_alert', 12),
        Field('vbat_lo_alert', 11),
        Field('vbat_hi_alert', 10),
        Field('vin_lo_alert', 9),
        Field('vin_hi_alert', 8),
        Field('vsys_lo_alert', 7),
        Field('vsys_hi_alert', 6),
        Field('iin_hi_alert', 5),
        Field('ibat_lo_alert', 4),
        Field('die_temp_hi_alert', 3),
        Field('bst_hi_alert', 2),
        Field('ntc_ratio_hi_alert', 1),
        Field('ntc_ratio_lo_alert', 0)]),
    Register(0x37, value=0, name='CHARGER_STATE_ALERTS', **defs, fields=[
        Field('equalize_charge_alert', 10),
        Field('absorb_charge_alert', 9),
        Field('charger_suspended_alert', 8),
        Field('precharge_alert', 7),
        Field('cc_cv_charge_alert', 6),
        Field('ntc_pause_alert', 5),
        Field('timer_term_alert', 4),
        Field('c_over_x_term_alert', 3),
        Field('max_charge_time_fault_alert', 2),
        Field('bat_missing_fault_alert', 1),
        Field('bat_short_fault_alert', 0)]),
    Register(0x38, value=0, name='CHARGER_STATUS_ALERTS', **defs, fields=[
        Field('vin_uvcl_active_alert', 3),
        Field('iin_limit_active_alert', 2),
        Field('constant_current_alert', 1),
        Field('constatn_voltage_alert', 0)]),
    Register(0x39, value=0, name='SYSTEM_STATUS', **defs, fields=[
        Field('charge_enabled', 13),
        Field('mppt_en_pin', 11),
        Field('equalize_req', 10),
        Field('drvcc_good', 9),
        Field('cell_count_error', 8),
        Field('ok_to_charge', 6),
        Field('no_rt', 5),
        Field('thermal_shutdown', 4),
        Field('vin_ovlo', 3),
        Field('vin_gt_bat', 2),
        Field('intvcc_gt_4p3v', 1),
        Field('intvcc_gt_2p8v', 0)]),
    Register(0x3a, value=0, name='VBAT', **defs, fields=[
        Field('vbat', 15, 0, fn=lambda x: x * 0.000192264, unit='V')]),
    Register(0x3b, value=0, name='VIN', **defs, fields=[
        Field('vin', 15, 0, fn=lambda x: x * 0.001648, unit='V')]),
    Register(0x3c, value=0, name='VSYS', **defs, fields=[
        Field('vsys', 15, 0, fn=lambda x: x * 0.001648, unit='V')]),
    Register(0x3d, value=0, name='IBAT', **defs, fields=[
        Field('iin', 15, 0, fn=lambda x: x * 1.46487/0.004, unit='uA')]),
    Register(0x3e, value=0, name='IIN', **defs, fields=[
        Field('iin', 15, 0, fn=lambda x: x * 1.46487/0.003, unit='uA')]),
    Register(0x3f, value=0, name='DIE_TEMP', **defs, fields=[
        Field('die_temp', 15, 0, fn=lambda x: (x - 12010)/45.6, unit='C')]),
    Register(0x40, value=0, name='NTC_RATIO', **defs),
    Register(0x41, value=0, name='BSR', **defs),
    Register(0x42, value=0, name='JEITA_REGION', **defs),
    Register(0x43, value=0, name='CHEM_CELLS', **defs, fields=[
        Field('chem', 11, 8),
        Field('cell_count_pins', 3, 0)]),
    Register(0x44, value=0, name='ICHARGE_DAC', **defs, fields=[
        Field('icharge_dac', 4, 0)]),
    Register(0x45, value=0, name='VCHARGE_DAC', **defs, fields=[
        Field('vcharge_dac', 5, 0)]),
    Register(0x46, value=0, name='IIN_LIMIT_DAC', **defs, fields=[
        Field('iin_limit_dac', 5, 0)]),
    Register(0x47, value=0, name='VBAT_FILT', **defs),
    Register(0x48, value=0, name='ICHARGE_BSR', **defs),
    Register(0x4a, value=0, name='MEAS_SYS_VALID', **defs, fields=[
        Field('meas_sys_valid', 0)])
]
