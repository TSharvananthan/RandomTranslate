var slider = document.getElementById("main-slider");
var result_text = document.getElementById("text");
var language = document.getElementById("language");
var cycleCount = document.getElementById("cycleCount");
var values = JSON.parse('{{ text_dict | tojson | safe }}');

// Default
cycleCount.innerHTML = "Cycle: " + slider.value;
result_text.innerHTML = values[slider.value][0];
language.innerHTML = "Language: " + values[slider.value][1]

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  result_text.innerHTML = values[this.value][0];
  language.innerHTML = "Language: " + values[this.value][1]
  cycleCount.innerHTML = "Cycle: " + this.value;
}
