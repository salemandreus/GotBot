from django import forms

from .models import SupplyItem

class SupplyItemForm(forms.Form):
    name = forms.CharField()
    slug = forms.SlugField()
    notes = forms.CharField(widget=forms.Textarea)
    min_amount = forms.IntegerField(widget=forms.ChoiceField)
    med_amount = forms.IntegerField()
    max_amount = forms.IntegerField()

class SupplyItemModelForm(forms.ModelForm):
    class Meta:
        model = SupplyItem
        fields = ['name', 'code', 'image', 'slug', 'notes', 'min_amount', 'med_amount', 'max_amount']

    def clean_name(self, *args, **kwargs):
        instance=self.instance
        print(instance)
        name = self.cleaned_data.get('name')
        qs = SupplyItem.objects.filter(name__iexact=name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # exclude comparisons against itself
        if qs.exists():
            raise forms.ValidationError("This name has already been used. Please try another one.")
        return name

    def clean_slug(self, *args, **kwargs):
        instance = self.instance
        print(instance)
        slug = self.cleaned_data.get('slug')
        qs = SupplyItem.objects.filter(slug__iexact=slug) # backwards compatibility in slugs with uppercase exist since Django allows them by default without our validator

        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This slug has already been used. Please try another one.")
        return slug.lower()
