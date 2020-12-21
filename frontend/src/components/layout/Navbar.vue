<template>
  <nav>
    <ul>
      <router-link tag="li" :to="'/' + page.url" v-for="page in pages" :key="page.url" :class="{ selected: currentLocation.indexOf(page.url) > -1 }">
        <a>
          <Icon :name="page.icon" />
          <p>{{ $t('navbar.' + page.url) }}</p>
        </a>
      </router-link>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    page: {
      type: String,
      required: true
    }
  },
  data: function () {
    return {
      pages: [
        {
          url: 'recipes',
          icon: 'recipe'
        },
        {
          url: 'agenda',
          icon: 'menu'
        },
        {
          url: 'shopping',
          icon: 'list'
        }
      ],
      currentLocation: window.location.pathname
    }
  }
}
</script>

<style lang="scss" scoped>
nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--spacing-02);
  box-shadow: 0 -2px 4px 0 rgba(0, 0, 0, 0.1);
  background-color: var(--white);
  z-index: var(--depth-navbar);
}

ul {
  display: flex;
}

li {
  flex-basis: calc(100% / 3);
  border-radius: 5px;
  color: var(--grey-70);
  height: 4rem;

  a {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
  }

  i {
    color: var(--background-50);
    height: 1.5em;
    width: 1.5em;
  }

  p {
    margin: 0;
    margin-top: var(--spacing-01);
    font-size: 0.875em;
    font-weight: bold;
  }

  + li {
    margin-left: var(--spacing-02);
  }

  &:hover,
  &:focus,
  &.selected {
    color: var(--primary-60);
    background-color: var(--primary-40);

    i {
      color: var(--primary-50);
    }
  }
}
</style>
