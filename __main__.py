"""A Python Pulumi program to create a cpcode"""

import pulumi
import pulumi_akamai as akamai

# get information from our config file. 
# use "pulumi config set <key> [value]" to set the value
# Config is unique per stack to create new stack "pulumi stack init" and select it via "pulumi stack select"
config = pulumi.Config()
group_name = config.require("group_name")
cpcode_name = config.require("cpcode_name")

# we can export it or re-query it again in other stack
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

# create cpcode and using name as the export value in the next stack
# https://www.pulumi.com/docs/reference/pkg/akamai/cpcode/
# you can create a new cpcode but you can't remove it.
cpcode = akamai.CpCode(
    cpcode_name,
    contract_id=contract_id,
    group_id=group_id,
    name=cpcode_name,
    product=product_id
)

# share created vars with other stack so we don't need to recreate them
pulumi.export('cpcode_name', cpcode.name)