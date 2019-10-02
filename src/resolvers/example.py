from tartiflette import Resolver
from ..support import Ctx

@Resolver("Mutation.updateRecipe")
async def resolve_mutation_update_recipe(
    parent=dict(), args=dict(), ctx: Ctx=dict(), info=dict()
):
    return
