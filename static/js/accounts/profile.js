const profileClass = 'profile'
const thoughtSelectorEl = document.querySelector(`.${profileClass}__thoughts`)
const thoughtSelectorActiveClass = `${profileClass}__thoughts--active`
const commentsSelectorEl = document.querySelector(`.${profileClass}__comments`)
const commentSelectorActiveClass = `${profileClass}__comments--active`
const thoughtContainerEl = document.querySelector(`.${profileClass}__thoughts-container`)
const commentsContainerEl = document.querySelector(`.${profileClass}__comments-container`)

thoughtSelectorEl?.addEventListener('click', () => {
    thoughtContainerEl?.classList.remove('hidden');
    commentsContainerEl?.classList.contains('hidden') ? null : commentsContainerEl?.classList.add('hidden');

    thoughtSelectorEl?.classList.contains(thoughtSelectorActiveClass) ? null : thoughtSelectorEl?.classList.add(thoughtSelectorActiveClass);
    commentsSelectorEl?.classList.contains(commentSelectorActiveClass) ? commentsSelectorEl?.classList.remove(commentSelectorActiveClass) : null;
})

commentsSelectorEl?.addEventListener('click', () => {
    commentsContainerEl?.classList.remove('hidden');
    thoughtContainerEl?.classList.contains('hidden') ? null : thoughtContainerEl?.classList.add('hidden');

    commentsSelectorEl?.classList.contains(commentSelectorActiveClass) ? null : commentsSelectorEl?.classList.add(commentSelectorActiveClass);
    thoughtSelectorEl?.classList.contains(thoughtSelectorActiveClass) ? thoughtSelectorEl?.classList.remove(thoughtSelectorActiveClass) : null;
})