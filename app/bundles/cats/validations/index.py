from gettext import gettext as _

_errors = {
    'string': {
        "type": _("{{name}} must be a string"),
        "pattern": _("{{name}} is not in a valid format"),
        "default": _("{{name}} has something wrong"),
        "minLength": _("{{name}} is too short")
    }, 
    'integer': {
        "type": _("{{name}} must be an integer"),
        "pattern": _("{{name}} is not in a valid format"),
        "default": _("{{name}} has something wrong"),
        "minLength": _("{{name}} is too short"),
        "pattern": _("{{name}} must be an integer"),
    }
}

valid_cat = {
    "title": "Cat Schema",
    "type": "object",
    "properties": {
        "name": {
            "description": "Your cat's name",
            "type": "string",
            "errors": _errors['string'],
            "minLength": 1
        },
        "age": {
            "description": "Age in years",
            "type": "number", # "number" and "integer" don't work right now :BUG:
            "errors": _errors['integer']
        },
        "loves": {
            "description": "Things your cat loves",
            "type": "array",
            "minItems": 1,
            "items": { 
                "type": "string"
            },
            "uniqueItems": True,
            "errors": _errors['string']
        },
        "picture": {
            "description": "Link to a picture of your cat",
            "type": "string",
            "format": "uri",
            "errors": _errors['string']
        }
    },
    "required": ["name"],
    "errors": {
        "required": _("{{name}} is a required field"),
    } 
}