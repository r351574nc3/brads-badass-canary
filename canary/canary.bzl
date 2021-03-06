def _gen_arm_template_impl(ctx):
    """Generates an arm template. Currently doesn't support any resource types."""

    print("This rule does nothing...yet")

gen_arm_template = rule(implementation = _gen_arm_template_impl)


def _deploy_canary_impl(ctx):
    deploy = ctx.executable._deploy
    out = ctx.actions.declare_file(ctx.label.name + ".json")
    ctx.actions.run(
        executable = deploy,
        arguments = [
            ctx.label.name,
            out.path,
            ctx.attr.teams_connector_override,
            ctx.attr.sms_connector_override,
            ctx.attr.office365_connector_override
        ],
        inputs = [],
        tools = [ deploy ],
        outputs = [ out ],
        progress_message = "Deploying {} ...".format(ctx.label.name),
        use_default_shell_env = True,
    )
    return [DefaultInfo(files = depset([out]))]

deploy_canary = rule(
    implementation = _deploy_canary_impl,
    attrs = {
        "teams_connector_override": attr.string(),
        "office365_connector_override": attr.string(),
        "sms_connector_override": attr.string(),
        "_deploy": attr.label(
            default = Label("//canary:deploy"),
            allow_files = True,
            executable = True,
            cfg = "exec",
        ),
    },
)
