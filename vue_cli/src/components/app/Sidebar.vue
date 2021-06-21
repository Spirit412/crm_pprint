<template>
  <ul class="sidenav app-sidenav" :class="{open: value}">
    <router-link 
    v-for="link in links"
    :key="link.url"
    tag="li" 
    active-class="active" 
    :to="link.url"
    :exact="link.exact"
    >
      <a href="#" class="waves-effect waves-orange pointer">{{link.title}}</a>
    </router-link>
  </ul>
</template>

<script>
export default {
    props: ['value'],
    data: () => ({
        links: [
            {title: 'Счет', url: '/', exact: true},
            {title: 'Цифровые заказы', url: '/djobs'},
            {title: '+ цифровой заказ', url: '/djobadd'},
            {title: 'Таблица Z', url: '/zubs'},
            {title: '+ Z', url: '/zubadd'},
            {title: 'Таблица штампов', url: '/diecuts'},
            {title: '+ штамп', url: '/diecutadd'},
            {title: 'Новая запись', url: '/record'},
            {title: 'Заказчики', url: '/customers'},
        ]
    })
}
</script>