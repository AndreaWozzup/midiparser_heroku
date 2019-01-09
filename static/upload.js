const url = 'http://localhost:5000/upload';
const form = document.querySelector('form');

form.addEventListener('submit', e => {
    e.preventDefault();
    const formData = new FormData();

    let file = document.getElementById("file").files[0];  // file from input
    formData.append("file", file);

    fetch(url, {
        method: 'POST',
        body: formData
    }).then(response => response.json()
    ).then(data => {
        document.getElementById("title").innerHTML = data.title
        document.getElementById("length").innerHTML = data.length
        document.getElementById("bpm").innerHTML = data.bpm
        document.getElementById("body").innerHTML = data.body
        //document.getElementById("output").value=data
        console.log(data);
    });
});