{% include 'license.tpl' %}
{% include 'future.tpl' %}
{% include 'ansible_metadata.tpl' %}

def main():
    argument_spec = dict(
        {%- for color in params %}
        {{ color }},
        {%- endfor %}
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        support_check_mode=True,
    )

    module.get('{{ url }}')


if __name__ == '__main__':
    main()

