from importlib import import_module
import pkgutil

vertical_path = __path__


class Registry(object):
    verticals = {}

    def __getitem__(self, item):
        return self.verticals.get(item)

    def __contains__(self, item):
        return item in self.verticals

    def register(self, slug, vertical):
        assert slug not in self.verticals, 'Vertical is already registered.'
        vertical.slug = slug
        self.verticals[slug] = vertical

    def unregister(self, slug):
        self.verticals.pop(slug, None)

    def autoregister(self):
        for _, slug, _ in pkgutil.iter_modules(vertical_path):
            vertical = import_module('.' + slug, self.__class__.__module__)
            if self.is_valid(vertical):
                self.register(slug, vertical)

    def is_valid(self, vertical):
        return all([
            hasattr(vertical, 'PingDataSerializer'),
            hasattr(vertical, 'PostDataSerializer'),
        ])

    def get_choices(self):
        return [
            (slug, vertical.name)
            for slug, vertical in self.verticals.iteritems()
        ]

registry = Registry()
registry.autoregister()
