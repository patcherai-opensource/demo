export function renderPreview(input) {
  const preview = document.createElement("div");
  preview.innerHTML = input;
  return preview;
}
