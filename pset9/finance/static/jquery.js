{% extends layout.html %}

{% block script %}

    function greet()
    {
        let name = document.querySelector('#username').value;
        if (name === '')
        {
            alert('You must provide a name');
        }

    }
{% endblock %}