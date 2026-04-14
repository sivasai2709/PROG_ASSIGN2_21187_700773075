async function runNL() {
    const text = document.getElementById("input").value;

    const res = await fetch("/nlq", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await res.json();

    document.getElementById("output").innerText =
        "CYPHER:\n" + data.cypher + "\n\nRESULT:\n" +
        JSON.stringify(data.result, null, 2);
}

async function createNode() {
    const res = await fetch("/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            label: "Characters",
            props: {
                name: "Luke Skywalker",
                gender: "male",
                height: "172"
            }
        })
    });

    document.getElementById("crud-output").innerText =
        JSON.stringify(await res.json(), null, 2);
}

async function getAll() {
    const res = await fetch("/read/Characters");

    document.getElementById("crud-output").innerText =
        JSON.stringify(await res.json(), null, 2);
}
