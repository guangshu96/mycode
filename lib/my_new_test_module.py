#!/usr/bin/env python3

ANSIBLE_METADATA = {
        'metadata_version': '1.1',
        'status': ['preview'],
        'supported_by': 'community'
        }

DOCUMENTATION = '''
Build me later

'''

EXAMPLES = '''
write some exampls
'''

RETURN = '''
original_message:
    description: the original name parm that was passed in
    type: str
message:
    description: the output message that the sample module gerates
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False),
        turtle=dict(type='str', required=False, default='box'))

    result = dict(
            changed=False,
            original_message='',
            message='')    

    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True)

    if module.check_mode:
        return results

    result['original_message'] = module.params['name'] 
    result['message'] = 'hello' + module.params['name'] + ' pleasure to meet you!'

    if module.params['turtle'] != 'box':
        result['message'] = result['message'] + 'wow your' + module.params['turtle'] + ' turtle is a cutie'

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'hughes':
        result['message'] += ' and you work at hughes! '

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requeste this to fail', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()


