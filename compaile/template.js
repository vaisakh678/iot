const objs = {"replace-code-here-mf"};
const element = document.querySelector('.editor__component_picker__groups__btn__container');
const input = document.querySelector('.js-analytics.ui-autocomplete-input');
let count = 0;
const arr = Object.keys(objs);
element.addEventListener('click', () => {
    const name = arr[count % arr.length];
    input.value = name;
    localStorage.setItem("circuitClipboard", objs[name]);
    console.log(name);
    count++;
});