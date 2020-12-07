def _gen_arm_template_impl(ctx):
    """Generates an arm template. Currently doesn't support any resource types."""

    print("This rule does nothing...yet")

gen_arm_template = rule(implementation = _gen_arm_template_impl)

def _deploy_arm_template_impl(ctx):
    """Takes an existing arm template and deploys it."""
    print("Doing deploy")

deploy_arm_template = rule(implementation = _deploy_arm_template_impl)

"""Minimalist example of a rule that does nothing."""

def _empty_impl(ctx):
    # This function is called when the rule is analyzed.
    # You may use print for debugging.
    print("This rule does nothing")

empty = rule(implementation = _empty_impl)