// generate slug in form field from its identifier (pk) code field
const codeInput = document.querySelector('input[name=code');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-') // replacing & with '-and-'
        .replace(/[\s\W-]+/g, '-') //replacing spaces, non-word chars and dashes with a single '-'
        .replace(/^\W+/g,'') //remove start char if not a word char
        .replace(/\W+$/g,'') //remove end char if not a word char
};

codeInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(codeInput.value));
});