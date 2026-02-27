#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/aristotle

# Display
TARGET_SCREEN_DENSITY := 440

BOARD_VENDOR_KERNEL_MODULES_LOAD := $(strip $(shell cat $(DEVICE_PATH)/modules/modules.load))

# Properties
TARGET_SYSTEM_EXT_PROP += $(DEVICE_PATH)/system_ext.prop
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop
TAGET_SYSTEM_PROP += $(DEVICE_PATH)/system.prop

# SPL
BOOT_SECURITY_PATCH := 2026-01-08
VENDOR_SECURITY_PATCH := $(BOOT_SECURITY_PATCH)

# Inherit from mt6895-common
include device/xiaomi/mt6895-common/BoardConfigCommon.mk

# Inherit the proprietary files
include vendor/xiaomi/aristotle/BoardConfigVendor.mk