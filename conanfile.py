from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = "ffmpeg/5.1.3"
    default_options = {
        "ffmpeg/*:shared": True,
        "ffmpeg/*:with_asm": False,
        "ffmpeg/*:with_zlib": False,
        "ffmpeg/*:with_bzip2": False,
        "ffmpeg/*:with_lzma": False,
        "ffmpeg/*:with_libiconv": False,
        "ffmpeg/*:with_freetype": False,
        "ffmpeg/*:with_openjpeg": False,
        "ffmpeg/*:with_openh264": False,
        "ffmpeg/*:with_opus": False,
        "ffmpeg/*:with_vorbis": False,
        "ffmpeg/*:with_zeromq": False,
        "ffmpeg/*:with_sdl": False,
        "ffmpeg/*:with_libx264": False,
        "ffmpeg/*:with_libx265": False,
        "ffmpeg/*:with_libvpx": False,
        "ffmpeg/*:with_libmp3lame": False,
        "ffmpeg/*:with_libfdk_aac": False,
        "ffmpeg/*:with_libwebp": False,
        "ffmpeg/*:with_ssl": "openssl",
        "ffmpeg/*:with_libalsa": False,
        "ffmpeg/*:with_pulse": False,
        "ffmpeg/*:with_vaapi": False,
        "ffmpeg/*:with_vdpau": False,
        "ffmpeg/*:with_vulkan": False,
        "ffmpeg/*:with_xcb": False,
        "ffmpeg/*:with_appkit": False,
        "ffmpeg/*:with_avfoundation": False,
        "ffmpeg/*:with_coreimage": False,
        "ffmpeg/*:with_audiotoolbox": False,
        "ffmpeg/*:with_videotoolbox": False,
        "ffmpeg/*:with_programs": False,
        "ffmpeg/*:with_libsvtav1": False,
        "ffmpeg/*:with_libaom": False,
        "ffmpeg/*:with_libdav1d": False,
        "ffmpeg/*:with_libdrm": False,
        "ffmpeg/*:with_jni": False,
        "ffmpeg/*:with_mediacodec": False,
        "ffmpeg/*:with_xlib": False
    }

    def layout(self):
        cmake_layout(self)