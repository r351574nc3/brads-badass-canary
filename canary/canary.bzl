def _gen_arm_template_impl(ctx):
    """Generates an arm template. Currently doesn't support any resource types."""

    print("This rule does nothing...yet")

gen_arm_template = rule(implementation = _gen_arm_template_impl)

def _deploy_canary_impl(ctx):
    """Takes an existing arm template and deploys it."""
    args = [ctx.label.name]
    log = ctx.actions.declare_file("{}.log".format(ctx.label.name))

    # Action to call the script.
    ctx.actions.run(
        inputs = [],
        outputs = [log],
        arguments = args,
        progress_message = "Deploying {} ...".format(ctx.label.name),
        use_default_shell_env = True,
        executable = ctx.executable.deploy_tool,
    )

deploy_canary = rule(
    implementation = _deploy_canary_impl,
    attrs = {
        "deploy_tool": attr.label(
            executable = True,
            cfg = "exec",
            allow_files = True,
            default = Label("//canary:deploy")
        )
    },
    executable = True
)
