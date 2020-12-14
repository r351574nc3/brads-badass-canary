def _gen_arm_template_impl(ctx):
    """Generates an arm template. Currently doesn't support any resource types."""

    print("This rule does nothing...yet")

gen_arm_template = rule(implementation = _gen_arm_template_impl)


def _deploy_canary_impl(ctx):
    deploy = ctx.executable._deploy
    out = ctx.outputs.out
    ctx.actions.run(
        executable = deploy,
        arguments = [ctx.label.name],
        inputs = [],
        tools = [deploy],
        outputs = [ out ],
        progress_message = "Deploying {} ...".format(ctx.label.name),
        use_default_shell_env = True,
    )

deploy_canary = rule(
    implementation = _deploy_canary_impl,
    attrs = {
        "_deploy": attr.label(
            default = Label("//canary:deploy"),
            allow_files = True,
            executable = True,
            cfg = "exec",
        ),
    },
    outputs = {"out": "%{name}.out"},
)
