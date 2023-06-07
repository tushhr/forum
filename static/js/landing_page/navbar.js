navbarClass = 'navbar';
signInButtonClass = `${navbarClass}__signin`;
signUpButtonClass = `${navbarClass}__signup`;

signInModalClass = 'signin-modal';
signUpModalClass = 'signup-modal';

signInButton = document.querySelector(`.${signInButtonClass}`);
signUpButton = document.querySelector(`.${signUpButtonClass}`);
signInModal = document.querySelector(`.${signInModalClass}`);
signUpModal = document.querySelector(`.${signUpModalClass}`);
signInTrigger = document.querySelector(`.${signUpModalClass}__signin-trigger`);
signUpTrigger = document.querySelector(`.${signInModalClass}__signup-trigger`);
signInOverlay = document.querySelector(`.${signInModalClass}__overlay`);
signUpOverlay = document.querySelector(`.${signUpModalClass}__overlay`);

signInTogglers = [signInButton, signInTrigger, signInOverlay]
signUpTogglers = [signUpButton, signUpTrigger, signUpOverlay]

const toggleSignInModal = () => {
    if(signInModal?.classList.contains('hidden')){
        signInModal.classList.remove('hidden');

        if(!signUpModal?.classList.contains('hidden')) {
            signUpModal?.classList.add('hidden');
        }
    }
    else {
        signInModal?.classList.add('hidden');
    }
}

const toggleSignUpModal = () => {
    if(signUpModal?.classList.contains('hidden')){
        signUpModal.classList.remove('hidden');

        if(!signInModal?.classList.contains('hidden')) {
            signInModal?.classList.add('hidden');
        }
    }
    else {
        signUpModal?.classList.add('hidden');
    }
}

signInTogglers.forEach(signInToggler => {
    signInToggler.addEventListener('click', () => {
        toggleSignInModal();
    })
})

signUpTogglers.forEach(signUpToggler => {
    signUpToggler.addEventListener('click', () => {
        toggleSignUpModal();
    })
})