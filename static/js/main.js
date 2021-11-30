function generate() {
    $.ajax({
        url: "/generate",
        type: "POST",
        dataType: "json",
        success: function (data) {
            update(data.name)
        }
    });
}

function update(name) {
    $.ajax({
        url: "/" + name,
        type: "POST",
        dataType: "json",
        success: function (data) {
            var img = data.sprites.other.dream_world.front_default;
            if (img) {
                $("#sprite").attr("src", data.sprites.other.dream_world.front_default);
            }
            $("#name").text(data.name.toUpperCase())
            $("#id").text(data.id)
            $("#type").text(data.types[0].type.name.toUpperCase())
        }
    });
}