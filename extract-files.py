#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/mediatek/libaedv',
    'hardware/xiaomi',
]

blob_fixups: blob_fixups_user_type = {
    'system_ext/priv-app/ImsService/ImsService.apk': blob_fixup()
        .apktool_patch('blob-patches/ImsService/0001-ImsService-Export-receivers-that-aren-t-exclusively-.patch')
        .apktool_patch('blob-patches/ImsService/0002-ImsService-Switch-to-shared-libs-to-mtk-frameworks.patch')
        .apktool_patch('blob-patches/ImsService/0003-ImsService-Remove-references-to-TelephonyMetrics.patch'),
    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),
    # Блок для libsink-mtk.so здесь больше не нужен, так как мы добавили DISABLE_CHECKELF в текстовый файл
    ('system_ext/etc/init/init.vtservice.rc', 'vendor/etc/init/android.hardware.neuralnetworks-shim-service-mtk.rc'): blob_fixup()
        .regex_replace('start', 'enable'),
    'vendor/etc/vintf/manifest/manifest_media_c2_V1_2_default.xml': blob_fixup()
        .regex_replace('1.1', '1.2'),
    'vendor/etc/public.libraries.txt': blob_fixup()
        .add_line_if_missing('libmpbase.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    'vendor/lib64/hw/sensors.mediatek.V2.0.so': blob_fixup()
       .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libcodec2_hidl@1.0-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v35.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.1-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v35.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.2-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v35.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl_plugin-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    ('vendor/lib64/libcodec2_mtk_c2store.so', 'vendor/lib64/libcodec2_vpp_dump_mtk_yuv_plugin.so', 'vendor/lib64/libcodec2_vpp_gc_plugin.so', 'vendor/lib64/libcodec2_vpp_qt_plugin.so', 'vendor/lib64/libcodec2_vpp_rs_plugin.so'): blob_fixup()
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libdolbyplugin.so': blob_fixup()
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libui.so', 'libui-v34.so'),
    ('vendor/lib64/libcodec2_mtk_vdec.so', 'vendor/lib64/libcodec2_mtk_venc.so', 'vendor/lib64/libcodec2_vpp_dolby_plugin.so'): blob_fixup()
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libui.so', 'libui-v34.so'),
    'vendor/lib64/libcodec2_soft_common-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so'),
    'vendor/lib64/libcodec2_vndk-v31.so': blob_fixup()
        .replace_needed('libui.so', 'libui-v34.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libsfplugin_ccodec_utils-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/bin/hw/android.hardware.security.keymint@1.0-service.beanpod': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V4-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so'),
    'vendor/bin/hw/android.hardware.security.keymint@1.0-service.mitee': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V4-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so'),
    (
        'vendor/bin/camerahalserver', 
        'vendor/bin/hw/camerahalserver', 
        'odm/bin/camerahalserver', 
        'odm/bin/hw/camerahalserver', 
        'vendor/bin/hw/mt6895/camerahalserver',
        'vendor/lib64/libmtkcam_hal_aidl_provider.so'
    ): blob_fixup()
        .replace_needed('android.hardware.camera.provider-V1-ndk_platform.so', 'android.hardware.camera.provider-V1-ndk.so'),
    ('vendor/lib64/libmtkcam_hal_aidl_device.so', 'vendor/lib64/libmtkcam_hal_aidl_utils.so'): blob_fixup()
        .replace_needed('android.hardware.camera.device-V1-ndk_platform.so', 'android.hardware.camera.device-V1-ndk.so'),
    'vendor/lib64/libmtkcam_hal_aidl_common.so': blob_fixup()
        .replace_needed('android.hardware.camera.common-V1-ndk_platform.so', 'android.hardware.camera.common-V1-ndk.so')
        .replace_needed('android.hardware.camera.device-V1-ndk_platform.so', 'android.hardware.camera.device-V1-ndk.so'),
    'vendor/lib64/libmt_mitee@1.3.so': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V4-ndk.so'),
    'vendor/bin/hw/mtkfusionrild' : blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/lib64/hw/mt6895/vendor.mediatek.hardware.pq@2.15-impl.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so')
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    ('vendor/lib64/mt6895/libaalservice.so', 'vendor/bin/mnld'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    'vendor/lib64/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/librt_extamp_intf.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    'vendor/lib64/mt6895/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),
    ('vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libteei_daemon_vfs.so': blob_fixup()
        .add_needed('liblog.so'),
    ('vendor/lib64/libwvhidl.so', 'vendor/lib64/mediadrm/libwvdrmengine.so'): blob_fixup()
        .replace_needed('libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-lite.so'),
    (
        'vendor/lib64/mt6895/lib3a.flash.so',
        'vendor/lib64/mt6895/lib3a.sensors.color.so',
        'vendor/lib64/mt6895/lib3a.sensors.flicker.so',
    ): blob_fixup()
        .add_needed('liblog.so'),
    (
        'vendor/lib64/mt6895/libcam.hal3a.ctrl.so',
        'vendor/lib64/mt6895/libcam.hal3a.so',
        'vendor/lib64/libmialgoengine.so',
        'vendor/lib64/mt6895/libmtkcam_request_requlator.so',
    ): blob_fixup()
        .add_needed('libprocessgroup.so')
        .add_needed('libcgrouprc.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'aristotle',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()