[
    {
        "name": "vpe",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "vip": "172.16.1.100"
        },
        "attributes": [
            "SAI_VIP_ENTRY_ATTR_ACTION",
            "SAI_VIP_ENTRY_ACTION_ACCEPT"
        ]
    },
    {
        "name": "dle",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "vni": "100"
        },
        "attributes": [
            "SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION",
            "SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION"
        ]
    },
    {
        "name": "in_acl_group_id",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_DASH_ACL_GROUP",
        "attributes": [
            "SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY",
            "SAI_IP_ADDR_FAMILY_IPV4"
        ]
    },
    {
        "name": "out_acl_group_id",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_DASH_ACL_GROUP",
        "attributes": [
            "SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY",
            "SAI_IP_ADDR_FAMILY_IPV4"
        ]
    },
    {
        "name": "vnet",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_VNET",
        "attributes": [
            "SAI_VNET_ATTR_VNI",
            "1000"
        ]
    },
    {
        "name": "eni",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_ENI",
        "attributes": [
            "SAI_ENI_ATTR_CPS",
            "10000",
            "SAI_ENI_ATTR_PPS",
            "100000",
            "SAI_ENI_ATTR_FLOWS",
            "100000",
            "SAI_ENI_ATTR_ADMIN_STATE",
            "True",
            "SAI_ENI_ATTR_VM_UNDERLAY_DIP",
            "172.16.1.1",
            "SAI_ENI_ATTR_VM_VNI",
            "9",
            "SAI_ENI_ATTR_VNET_ID",
            "$vnet",
            "SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID",
            "0",
            "SAI_ENI_ATTR_V4_METER_POLICY_ID",
            "0",
            "SAI_ENI_ATTR_V6_METER_POLICY_ID",
            "0"
        ]
    },
    {
        "name": "eam",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "address": "00:CC:CC:CC:00:00"
        },
        "attributes": [
            "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID",
            "$eni"
        ]
    },
    {
        "name": "ore",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "eni_id": "$eni",
            "destination": "10.1.0.0/16"
        },
        "attributes": [
            "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION",
            "SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET",
            "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID",
            "$vnet",
            "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_POLICY_EN",
            "False",
            "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_CLASS",
            "0"
        ]
    },
    {
        "name": "ocpe",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "dst_vnet_id": "$vnet",
            "dip": "10.1.2.50"
        },
        "attributes": [
            "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP",
            "172.16.1.20",
            "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC",
            "00:DD:DD:DD:00:00",
            "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI",
            "True",
            "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS",
            "0",
            "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS_OVERRIDE",
            "False"
        ]
    },
    {
        "name": "route_entry_1",
        "op": "create",
        "type": "SAI_OBJECT_TYPE_ROUTE_ENTRY",
        "key": {
            "switch_id": "$SWITCH_ID",
            "vr_id": "10",
            "destination": "0.0.0.0/0"
        },
        "attributes": [
            "SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID",
            "1"
        ]
    }
]