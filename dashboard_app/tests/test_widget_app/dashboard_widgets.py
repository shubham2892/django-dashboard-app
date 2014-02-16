"""
DummyWidget implementation used by the tests.

"""
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import datetime, now

from dashboard_app.widget_base import DashboardWidgetBase
from dashboard_app.widget_pool import dashboard_widget_pool


class DummyWidget(DashboardWidgetBase):
    """This widget is used by the tests."""
    template_name = 'test_widget_app/dummy_widget.html'
    settings = {
        'VALUE': {
            'verbose_name': _('Value'),
        }
    }

    def get_context_data(self):
        ctx = super(DummyWidget, self).get_context_data()
        value_setting = self.get_setting('VALUE')
        date = 'Widget has not been saved, yet...'
        if value_setting is not None:
            value = value_setting.value
            date = datetime.strptime(value, self.time_format)
        ctx.update({
            'value': date,
        })
        return ctx

    def update_widget_data(self):
        value = now().strftime(self.time_format)
        self.save_setting('VALUE', value)


class DummyWidget2(DashboardWidgetBase):
    """This widget is used by the tests."""
    template_name = 'test_widget_app/dummy_widget2.html'

    def get_context_data(self):
        ctx = super(DummyWidget2, self).get_context_data()
        ctx.update({
            'value': 'Barfoo',
        })
        return ctx

    def update_widget_data(self):
        pass


dashboard_widget_pool.register_widget(DummyWidget)
dashboard_widget_pool.register_widget(DummyWidget2)
