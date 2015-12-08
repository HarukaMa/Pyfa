# energyNosferatuFalloff
#
# Used by:
# Modules from group: Energy Nosferatu (45 of 45)
type = "active", "projected"
runTime = "late"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("powerTransferAmount")
    time = module.getModifiedItemAttr("duration")
    if "projected" in context:
        fit.addDrain(time, amount, 0)
    elif "module" in context:
        module.itemModifiedAttributes.force("capacitorNeed", -amount)