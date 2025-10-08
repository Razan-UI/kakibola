function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-dark-color', 'border-dark-color', 'text-dark-color',
        'bg-success-color', 'border-success-color', 'text-success-color',
        'bg-error-color', 'border-error-color', 'text-error-color',
        'bg-neutral-color', 'border-neutral-color', 'text-neutral-color'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-[#A67C6D]', 'border-[#A67C6D]', 'text-[#2E2A2B]');
        toastComponent.style.border = '1px solid #A67C6D';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-[#F2E1D4]', 'border-[#F2E1D4]', 'text-[#4B3D3D]');
        toastComponent.style.border = '1px solid #F2E1D4';
    } else { // neutral
        toastComponent.classList.add('bg-[#D9C6B2]', 'border-[#D9C6B2]', 'text-[#2E2A2B]');
        toastComponent.style.border = '1px solid #D9C6B2';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}