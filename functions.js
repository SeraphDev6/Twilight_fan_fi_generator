const form = document.getElementById("main_form")
const text = document.getElementById("storyStart")
const final =  document.getElementById("finalStory")

form.addEventListener("submit",(e)=>{
  e.preventDefault();
  const start = text.value;
  const size = document.querySelector('input[name="size"]:checked').value;
  fetch(`https://twilightify.herokuapp.com/?q=${encodeURIComponent(start)}&chars=${size}`)
  .then(res => res.json())
  .then(data => data.result)
  .then(data => final.innerText = data)
  .catch(e => console.log(e))
})