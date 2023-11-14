import os


templates = ["feed", "register", "login", "logout", "user_profile", "update_user_profile", "delete_user_profile", "excuses", "excuse", "excuse_categories", "excuse_category", "create_excuse", "update_excuse", "delete_excuse"]
for template in templates:
    os.system("cd ..")
    with open(f"fiesta/templates/fiesta/{template}.html", "w") as template_file:
        template_file.write("""

{% extends "layout.html" %}

{% block content %}
    
{% endblock content %}
                            
""")