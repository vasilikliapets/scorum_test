
get_block_payload = '{"method": "call", "id": 1, "params": ["database_api", "get_block", [1]], "jsonrpc": "2.0"}'

get_block_payload_bad_method = '{"method": "bad_method", "id": 1, ' \
                               '"params": ["database_api", "get_block", [1]], "jsonrpc": "2.0"}'

get_block_payload_bad_id = '{"method": "call", "id": "bad_id", ' \
                           '"params": ["database_api", "get_block", [1]], "jsonrpc": "2.0"}'

get_block_payload_bad_params = '{"method": "call", "id": 1, ' \
                               '"params": ["bad_params"], "jsonrpc": "2.0"}'


dynamic_payload = '{"method": "call", "id": 0, "params": ["database_api", "get_dynamic_global_properties", []],' \
                '"jsonrpc": "2.0"}'

dynamic_payload_bad_id = '{"method": "call", "id": "wrong_id", ' \
                         '"params": ["database_api", "get_dynamic_global_properties", []], "jsonrpc": "2.0"}'

dynamic_payload_bad_method = '{"method": "bad_method", "id": 0, ' \
                         '"params": ["database_api", "get_dynamic_global_properties", []], "jsonrpc": "2.0"}'

dynamic_payload_bad_params = '{"method": "call", "id": 0, ' \
                         '"params": ["bad_params"], "jsonrpc": "2.0"}'
