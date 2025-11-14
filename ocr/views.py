from django.shortcuts import render
from django.core.files.storage import default_storage
from .services.ocr_reader import extract_text

def ocr_page(request):
    context = {}

    if request.method == "POST" and request.FILES.get("image"):
        file = request.FILES["image"]

        # save temporarily
        path = default_storage.save(file.name, file)
        full_path = default_storage.path(path)

        # OCR
        extracted = extract_text(full_path)
        context["text"] = "\n".join(extracted)

    return render(request, "ocrapp/ocr_form.html", context)
