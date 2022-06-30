const form = document.getElementById("main_form")
const text = document.getElementById("storyStart")
const final =  document.getElementById("finalStory")
const submit = document.getElementById("submit")
form.addEventListener("submit",(e)=>{
  e.preventDefault();
  const start = text.value;
  const size = document.querySelector('input[name="size"]:checked').value;
  submit.disabled = true;
  fetch(`https://twilightify.herokuapp.com/?q=${encodeURIComponent(start)}&chars=${size}`)
  .then(res => res.json())
  .then(data => data.result)
  .then(data => final.innerText = data)
  .then(() => setTimeout(()=> submit.disabled = false, 1000))
  .catch(e => console.log(e))
})