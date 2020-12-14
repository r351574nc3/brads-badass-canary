load("@canary_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")
package(default_visibility = ["//visibility:public"])


py_library(
    name = "library",
    srcs = [
        "__init__.py",
    ],
    data = [
        ":logic-app-deployment-tpl.json", 
        ":api-connection-deployment-tpl.json"
    ]
)
