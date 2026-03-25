function load_devices(filename) {
    let data = [
        {"id": 1, "name": "Monitor", "state": "ok"},
        {"id": 2, "name": "Televize", "state": ""},
        {"id": 3, "name": "Telefon", "state": ""}
    ];

    let result = [];

    for (let i = 0; i < data.length; i++) {
        if (data[i].state != "") {
            result.push(data[i]);
        }
    }

    return result;
}

function sort_devices(device_list) {
    return device_list.sort(function(a, b) {
        if (a.name < b.name) return -1;
        if (a.name > b.name) return 1;
        return 0;
    });
}

function group_devices(device_list, limit) {
    let groups = [];
    let temp = [];

    for (let i = 0; i < device_list.length; i++) {
        temp.push(device_list[i]);

        if (temp.length == limit) {
            groups.push(temp);
            temp = [];
        }
    }

    if (temp.length > 0) {
        groups.push(temp);
    }

    return groups;
}

let devices = load_devices();
devices = sort_devices(devices);
let grouped = group_devices(devices, 2);

console.log(devices);
console.log(grouped);

document.getElementById("form").addEventListener("submit", function(e) {
    e.preventDefault();

    let name = document.getElementById("name").value.trim();
    let type = document.getElementById("type").value;

    if (name == "") return;

    let div = document.createElement("div");
    div.className = "karty";

    div.innerHTML = `
        <h2>${name}</h2>
        <p>${type}</p>
        <p>Funkční</p>
        <button>Detail</button>
    `;

    document.querySelector(".container").appendChild(div);

    document.getElementById("form").reset();
});