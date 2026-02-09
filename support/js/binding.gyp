{
    "targets": [
        {
            "target_name": "addon-ed25519",
            "sources": ["addon.cpp"],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "defines": [
                "NAPI_DISABLE_CPP_EXCEPTIONS",
                "FROST_LIB_HEADER=\"../../frost-ed25519/frost-ed25519-lib.h\""
            ],
            "dependencies": [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            "conditions": [
                ["OS=='mac'", {
                    "libraries": [ "<(module_root_dir)/../../target/release/libfrost_ed25519.dylib" ],
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "CLANG_CXX_LIBRARY": "libc++",
                        "MACOSX_DEPLOYMENT_TARGET": "10.15"
                    }
                }],
                ["OS=='linux'", {
                    "libraries": [ "<(module_root_dir)/../../target/release/libfrost_ed25519.so" ],
                    "cflags!": ["-fno-exceptions"],
                    "cflags_cc!": ["-fno-exceptions"]
                }]
            ]
        },
        {
            "target_name": "addon-secp256k1",
            "sources": ["addon.cpp"],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "defines": [
                "NAPI_DISABLE_CPP_EXCEPTIONS",
                "FROST_LIB_HEADER=\"../../frost-secp256k1/frost-secp256k1-lib.h\""
            ],
            "dependencies": [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            "conditions": [
                ["OS=='mac'", {
                    "libraries": [ "<(module_root_dir)/../../target/release/libfrost_secp256k1.dylib" ],
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "CLANG_CXX_LIBRARY": "libc++",
                        "MACOSX_DEPLOYMENT_TARGET": "10.15"
                    }
                }],
                ["OS=='linux'", {
                    "libraries": [ "<(module_root_dir)/../../target/release/libfrost_secp256k1.so" ],
                    "cflags!": ["-fno-exceptions"],
                    "cflags_cc!": ["-fno-exceptions"]
                }]
            ]
        },
        {
            "target_name": "addon-secp256k1-tr",
            "sources": ["addon.cpp"],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "defines": [
                "NAPI_DISABLE_CPP_EXCEPTIONS",
                "FROST_LIB_HEADER=\"../../frost-secp256k1-tr/frost-secp256k1-tr-lib.h\""
            ],
            "dependencies": [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            "conditions": [
                ["OS=='mac'", {
                    "libraries": [ "<(module_root_dir)/../../target/release/libfrost_secp256k1_tr.dylib" ],
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "CLANG_CXX_LIBRARY": "libc++",
                        "MACOSX_DEPLOYMENT_TARGET": "10.15"
                    }
                }],
                ["OS=='linux'", {
                    "libraries": [ "<(module_root_dir)/../../target/release/libfrost_secp256k1_tr.so" ],
                    "cflags!": ["-fno-exceptions"],
                    "cflags_cc!": ["-fno-exceptions"]
                }]
            ]
        }
    ]
}