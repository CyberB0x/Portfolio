
const tbody = document.getElementById('imagesTableBody');
fetch('/api/images').then(response => response.json()).then(images => setImages(images.images));

function setImages(images) {
    const imagesContainer = document.createElement('div');
    images.forEach(image => {
        const tr = document.createElement('tr');

        const tdPreview = document.createElement('td');
        const tdUrl = document.createElement('td');
        const tdDelete = document.createElement('td');

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-btn');
        deleteButton.textContent = 'X';
        tdDelete.appendChild(deleteButton);
        tdPreview.innerHTML = `<img src="/images/${image}" width="42" height="100%">`;
        tdUrl.innerHTML = `<a href="/images/${image}" target="_blank">${image}</a>`;

        tr.appendChild(tdPreview);
        tr.appendChild(tdUrl);
        tr.appendChild(tdDelete);

        tbody.appendChild(tr);
    });
    document.body.appendChild(imagesContainer);
}

document.getElementById('btnGoToUpload').addEventListener('click', (event) => {
    window.location.href = '/upload/';
});

