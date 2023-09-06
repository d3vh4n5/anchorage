document.getElementById('sidebarToggle').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('active');
    document.body.classList.toggle('active-sidebar');
    // document.querySelector('.main').classList.toggle('expanded-main');
    document.querySelector('.contenido-principal').classList.toggle('contenido-encoger')
});