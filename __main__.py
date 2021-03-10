"""A Python Pulumi program"""

import pulumi
import pulumi_akamai as akamai

# should use ENV to share between stacks
group_name = "GSS Training Internal-C-1IE2OHM"
cpcode_name = "jgrinwis-pristine"

# we can export it or re-query it again
contract_id = akamai.get_contracts().contracts[0].contract_id
group_id = akamai.get_group(contract_id=contract_id, group_name=group_name).id

# check products available on contract via
# first list contracts via: akamai pm lc
# lookup product on contract via : akamai pm lp -c <contract_id> 
product = 'dsa'

# engineering code names don't match product names
# below a list of products with their engineering names
# https://registry.terraform.io/providers/akamai/akamai/latest/docs/guides/appendix
products = {
    'dsa': 'prd_Site_Accel',
    'dsd': 'prd_Dynamic_Site_Del',
    'ion': 'prd_Fresca',
    'ion_p': 'prd_SPM'
}

# define the product id you want to use for your property
# this should match the template and cpcode 
# https://registry.terraform.io/providers/akamai/akamai/latest/docs/guides/appendix
product_id = products[product]

# cpcode = akamai.CpCode(
#     cpcode_name,
#     contract_id=contract_id,
#     group_id=group_id,
#     name=cpcode_name
#     product=product_id
# )

# for now set it statically
cpcode_id = 'cpc_763552'

# share created vars with other stack so we don't need to recreate them
# pulumi.export('cpcode_id', cpcode.id)
# pulumi.export('cpcode_id', cpcode_id)
# pulumi.export('product_id', product_id)
# pulumi.export('group_name', group_name)
pulumi.export('cpcode_name', cpcode_name)