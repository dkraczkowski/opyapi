from opyapi import api
from opyapi.api import info


def generate_openapi_doc():
    document = {"openapi": "3.0.2", "info": generate_info_block(api.Api)}
    document = {**document, **generate_paths_block(api.Api.components)}
    return document


def generate_info_block(api_info: api.Api) -> dict:
    document = {
        "title": api_info.title,
        "version": api_info.version,
        "description": api_info.description,
    }

    if api_info.terms_of_service:
        document["termsOfService"] = api_info.terms_of_service

    if api_info.contact:
        document["contact"] = generate_contact_block(api_info.contact)

    if api_info.license:
        document["license"] = generate_license_block(api_info.license)

    return {"info": document}


def generate_contact_block(contact: info.Contact) -> dict:
    return {"name": contact.name, "url": contact.url, "email": contact.email}


def generate_license_block(license: info.License) -> dict:
    return {"name": license.name, "url": license.url}


def generate_paths_block(components: list) -> dict:
    document = {}
    for component in components:
        if not isinstance(component, api.Operation):
            continue

    return document
