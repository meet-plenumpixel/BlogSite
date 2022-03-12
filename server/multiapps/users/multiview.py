from operator import attrgetter
from django.views.generic.edit import UpdateView

class MultiUpdateView(UpdateView):
  merge_context = dict()

  def __init__(self, model=None, fields=None, pk_kwarg=None, prefix=None):
    self.model = model
    self.fields = fields
    self.pk_kwarg = pk_kwarg
    self.prefix = prefix

  def get_context_data(self, **kwargs):
    for instance in self.__get_new_instance():
      instance.object = instance.get_object()
      context = super(MultiUpdateView,instance).get_context_data(**kwargs)
      MultiUpdateView.merge_context.update({instance.prefix+'form':context})
    print(MultiUpdateView.merge_context)
    return MultiUpdateView.merge_context

  def get(self, request, *args, **kwargs):
    return self.render_to_response(self.get_context_data())

  def __get_new_instance(self):
    for item in self.multi_model:
      new_instance = self.__class__(
        model=item.get('model', None),
        fields=item.get('fields', None),
        pk_kwarg=item.get('pk', None),
        prefix=item.get('form_prefix', None)
      )
      new_instance.request = self.request
      new_instance.args = self.args
      new_instance.kwargs = self.kwargs
      new_instance.kwargs[new_instance.pk_url_kwarg] = attrgetter(new_instance.pk_kwarg)(new_instance)

      yield new_instance
