# Utility functions related to providers

import importlib

import config


def get_provider_cls(sensor):
        provider_cls_name = sensor.__class__.__name__ + 'Provider'
        provider_module_name = provider_cls_name.lower()
        provider_module_path = (config.PROVIDERS_PACKAGE + '.' +
                                provider_module_name)
        try:
            module = importlib.import_module(provider_module_path)
        except ImportError:
            raise ImportError(f'Couldnt import module {provider_module_path}, '
                              f'please reffer to'
                              f'documentation on "How to add sensors"')
        provider_cls = getattr(module, provider_cls_name)
        return provider_cls
