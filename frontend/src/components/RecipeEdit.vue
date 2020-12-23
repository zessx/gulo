<template>
  <main class="container">
    <header>
      <router-link v-if="loaded" :to="'/recipes/' + recipe.pk">
        <Icon name="arrow" class="back reversed" />
      </router-link>
      <Button icon="check" type="success" class="validate" :label="$t('recipes.validate')" />
    </header>

    <Loader v-if="!loaded" />

    <article class="recipe" v-if="loaded">
      <img :src="picture" :alt="title">

      <div class="filter-meal">
        <ul>
          <li v-for="_dish in this.$store.state.recipes.dishes" :key="_dish">
            <input type="radio" name="dish" :id="_dish" :value="_dish" :checked="dish == _dish">
            <label :for="_dish">
              <Icon :name="formatDishIcon(_dish)" />
              <p>{{ $tc('recipes.' + _dish, 1) }}</p>
            </label>
          </li>
        </ul>
      </div>

      <InputText name="title" class="input-title"
        :placeholder="$t('recipes.placeholders.title')"
        :value="title" />

      <div class="meta">
        <div class="duration">
          <Icon name="timing" />
          <InputNumber name="timing" min="0" step="1"
            :placeholder="$t('recipes.placeholders.duration')"
            :value="duration" />
        </div>
        <div class="portions">
          <Icon name="portion" />
          <InputNumber name="portions" min="0" step="1"
            :placeholder="$t('recipes.placeholders.portions')"
            :value="portions" />
        </div>
      </div>

      <div class="ingredients">
        <ul>
          <li v-for="ingredient in ingredients" :key="ingredient.pk"
            class="ingredient"
            :data-ingredient="ingredient.pk"
            v-on:mouseleave="unfocusIngredient">
            <InputText class="input-ingredient-name" :name="'ingredient/' + ingredient.pk + '/name'"
              :placeholder="$t('recipes.placeholders.ingredient')"
              :value="ingredient.name"
              v-on:mouseover.native="focusIngredientName" />
            <InputNumber class="input-ingredient-quantity" :name="'ingredient/' + ingredient.pk + '/quantity'" min="0"
              :placeholder="$t('recipes.placeholders.quantity')"
              :value="ingredient.quantity"
              v-on:change.native="updateGhostField" />
            <InputText class="input-ingredient-quantity-ghost" :name="'ingredient/' + ingredient.pk + '/quantity-ghost'"
              :placeholder="$t('recipes.placeholders.quantity')"
              :value="ingredient.quantity ? ingredient.quantity + $tc('ingredients.units.' + ingredient.unit, ingredient.quantity) : null"
              v-on:mouseover.native="focusIngredientUnit" />

            <ul class="units">
              <li key="none">
                <input type="radio"
                  :name="'ingredient/' + ingredient.pk + '/unit'"
                  :id="'ingredient/' + ingredient.pk + '/unit/none'"
                  value=""
                  :checked="ingredient.unit == null"
                  v-on:change="updateGhostField">
                <label :for="'ingredient/' + ingredient.pk + '/unit/none'">
                  <Icon name="none" />
                </label>
              </li>
              <li v-for="unit in units" :key="unit">
                <input type="radio"
                  :name="'ingredient/' + ingredient.pk + '/unit'"
                  :id="'ingredient/' + ingredient.pk + '/unit/' + unit"
                  :value="unit"
                  :checked="ingredient.unit == unit"
                  v-on:change="updateGhostField">
                <label :for="'ingredient/' + ingredient.pk + '/unit/' + unit">
                  <p>{{ $tc('ingredients.units.' + unit, 1) }}</p>
                </label>
              </li>
            </ul>

            <Button icon="delete" type="error" size="small" class="delete-ingredient full centered"
              :label="$t('recipes.delete_ingredient')"
              v-on:click.native="deleteIngredient" />
          </li>
        </ul>

        <div class="add-ingredient">
          <Button icon="add" type="secondary" class="full centered"
            v-on:click.native="addIngredient" />
        </div>
      </div>

      <div class="steps">
        <Separator />

        <h2>{{ $t('recipes.making') }}</h2>
        <ol v-on:dragover="dragStepOver" v-on:drop="dropStep">
          <li v-for="step in steps" :key="step.pk" :id="'step/' + step.pk" draggable="true" v-on:dragstart="dragStepStart">
            <Icon name="drag" />
            <Textarea :name="'step/' + step.pk" :value="step.text" :placeholder="$t('recipes.placeholders.step')" />
          </li>
        </ol>

        <Button icon="add" type="secondary" class="add-step full centered"
          v-on:click.native="addStep" />
      </div>

<!--
      <div class="tags" v-if="recipe.tags.length > 0">
        <Separator />

        <Tag v-for="tag in recipe.tags" :key="tag.pk" data-type="secondary"
          :data-tag="tag.pk" :label="tag.name"
          v-on:click.native="searchByTag" />
      </div>
-->

      <div class="actions">
        <Button icon="delete" type="error" class="full centered"
          :label="$t('recipes.delete')"
          v-on:click.native="askDeletion" />

        <PopupConfirm icon="delete" type="error"
          :title="$t('recipes.delete_confirm.title')"
          :label="$t('recipes.delete_confirm.label')"
          v-if="deleting"
          v-on:cancel="cancelDeletion"
          v-on:confirm="confirmDeletion" />
      </div>
    </article>

    <Navbar page="recipes" />
  </main>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import formatDuration from '@/utils/formatDuration'
import formatDishIcon from '@/utils/formatDishIcon'
import randomId from '@/utils/randomId'

export default {
  name: 'RecipeEdit',
  data: function () {
    return {
      // Statuses
      loaded: false,
      deleting: false,

      // Data
      title: null,
      picture: null,
      dish: null,
      duration: null,
      portions: null,
      tags: [],
      ingredients: [],
      steps: [],

      // Utils
      draggingElement: null,
      units: [
        'cl',
        'l',
        'g',
        'kg',
        'tsp',
        'tbs',
        'pinch',
        'cup'
      ]
    }
  },
  computed: mapState({
    recipe: state => state.recipes.recipe
  }),
  methods: {
    formatDuration: function (duration) {
      return formatDuration({ duration })
    },
    formatDishIcon: function (dish) {
      return formatDishIcon({ dish })
    },

    // Ingredients
    addIngredient: function () {
      this.ingredients.push({
        pk: randomId(8),
        name: null,
        quantity: null,
        unit: null
      })
    },
    deleteIngredient: function (event) {
      const ingredientElement = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      if (ingredientElement) {
        const id = ingredientElement.getAttribute('data-ingredient')
        this.ingredients = this.ingredients.filter(
          ingredient => ingredient.pk !== id
        )
      }
    },
    focusIngredientName: function (event) {
      const ingredientElement = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      if (ingredientElement) {
        ingredientElement.classList.add('show-delete-button')
        // Delays class removal to avoid misclicks
        setTimeout(function () {
          ingredientElement.classList.remove('show-units')
        }, 1)
      }
    },
    focusIngredientUnit: function (event) {
      const ingredientElement = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      if (ingredientElement) {
        ingredientElement.classList.add('show-units')
        // Delays class removal to avoid misclicks
        setTimeout(function () {
          ingredientElement.classList.remove('show-delete-button')
        }, 1)
      }
    },
    unfocusIngredient: function (event) {
      const ingredientElement = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      if (ingredientElement) {
        // Delays class removal to avoid misclicks
        setTimeout(function () {
          ingredientElement.classList.remove('show-units')
          ingredientElement.classList.remove('show-delete-button')
        }, 1)
      }
    },
    updateGhostField: function (event) {
      const ingredientElement = event.target.tagName === 'LI' && event.target.classList.contains('ingredient')
        ? event.target
        : event.target.closest('li.ingredient')
      if (ingredientElement) {
        const ghost = ingredientElement.querySelector('.input-ingredient-quantity-ghost input')
        const fieldQuantity = ingredientElement.querySelector('.input-ingredient-quantity input')
        const fieldUnit = ingredientElement.querySelector('.units input:checked')
        ghost.value = [fieldQuantity.value, this.$tc('ingredients.units.' + fieldUnit.value, fieldQuantity.value)].join(' ')
      }
    },

    // Steps
    dragStepStart: function (event) {
      this.draggingElement = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      event.dataTransfer.effectAllowed = 'move'
      event.dataTransfer.setData('text/plain', null)
      this.draggingElement.classList.add('dragging')
    },
    dragStepOver: function (event) {
      event.preventDefault()
      const target = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      if (!target) {
        return
      }
      if (this.isBefore(this.draggingElement, target)) {
        target.parentNode.insertBefore(this.draggingElement, target)
      } else {
        target.parentNode.insertBefore(this.draggingElement, target.nextSibling)
      }
    },
    dropStep: function () {
      this.draggingElement.classList.remove('dragging')
      this.draggingElement = null
      this.reorderSteps()
      // TODO: handle drop outside dropzone (visual glitch)
    },
    isBefore: function (el1, el2) {
      if (!el1 || !el2) {
        return false
      }
      if (el2.parentNode === el1.parentNode) {
        for (var cur = el1.previousSibling; cur && cur.nodeType !== 9; cur = cur.previousSibling) {
          if (cur === el2) {
            return true
          }
        }
      }
      return false
    },
    addStep: function () {
      this.steps.push({
        pk: randomId(8),
        order: document.querySelectorAll('.steps li').length,
        text: null
      })
    },
    reorderSteps: function () {
      this.steps.map((step) => {
        const stepNode = document.getElementById('step/' + step.pk)
        step.order = Array.prototype.indexOf.call(stepNode.parentNode.childNodes, stepNode)
        return step
      })
    },

    // Recipe deletion
    askDeletion: function () {
      this.deleting = true
    },
    cancelDeletion: function () {
      this.deleting = false
    },
    confirmDeletion: function () {
      axios.delete('/api/recipes/' + this.recipe.pk)
        .then(response => {
          this.$store.commit('recipes/clearRecipe')
          this.$store.commit('notices/addNotice', {
            icon: 'check',
            type: 'success',
            message: 'recipes.delete_confirm.notice'
          })
          this.$router.push('/recipes')
        })
        .catch(e => { console.log(e) })
    }
  },
  created () {
    this.$store.dispatch('recipes/getRecipe', this.$route.params.id).then(() => {
      this.title = this.$store.state.recipes.recipe.title
      this.picture = this.$store.state.recipes.recipe.picture
      this.dish = this.$store.state.recipes.recipe.dish
      this.duration = this.$store.state.recipes.recipe.duration
      this.portions = this.$store.state.recipes.recipe.portions
      this.tags = this.$store.state.recipes.recipe.tags
      this.ingredients = this.$store.state.recipes.recipe.ingredients
      this.steps = this.$store.state.recipes.recipe.steps

      if (this.ingredients.length === 0) {
        this.addIngredient()
      }

      this.loaded = true
    })
  }
}
</script>

<style lang="scss" scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  padding: var(--spacing-05) var(--spacing-06);

  .back {
    color: var(--background-50);
    font-size: 1.5rem;
    transition: color var(--speed-normal);

    &:hover,
    &:focus {
      color: var(--background-60);
    }
  }
}

.recipe {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 var(--spacing-06);
  padding-bottom: calc(4rem + 2 * var(--spacing-02) + var(--spacing-06));

  img {
    display: block;
    width: calc(100% + 2 * var(--spacing-06));
    height: 12rem;
    object-fit: cover;
    object-position: center center;
    border-radius: 8px;
    padding: var(--spacing-02);
    padding-bottom: var(--spacing-06);
  }

  hr {
    margin: var(--spacing-06) 0;
  }

  .filter-meal {
    width: 100%;

    ul {
      display: flex;
    }

    li {
      flex-basis: calc(100% / 3);

      + li {
        margin-left: var(--spacing-02);
      }
    }

    input[type="radio"] {
      display: none;

      &:checked + label {
        color: var(--primary-60);
        background-color: var(--primary-40);
        box-shadow: none;

        i {
          color: var(--primary-50);
        }
      }
    }

    label {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-radius: 5px;
      color: var(--grey-70);
      background: var(--white);
      box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
      height: 4.5rem;

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
    }
  }

  .input-text {
    padding-left: 0;
    padding-right: 0;
  }

  .input-title {
    font-size: 1.5rem;
  }

  .meta {
    display: flex;
    width: 100%;

    .duration,
    .portions {
      display: flex;
      align-items: center;
      width: 50%;
    }

    .portions .input-number {
      padding-right: 0;
    }

    i {
      color: var(--background-40);
      font-size: 1.25rem;
    }
  }

  .ingredients {
    width: 100%;

    > ul > li {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      position: relative;
      width: calc(100% - 1.25rem - var(--spacing-02));
      margin-left: calc(1.25rem + var(--spacing-02));

      &::before {
        content: '';
        position: absolute;
        top: calc(var(--spacing-03) + (1.5rem - 0.5rem) / 2);
        left: calc(-0.375rem - 0.5rem - var(--spacing-02));
        display: block;
        flex-shrink: 0;
        width: 0.5rem;
        height: 0.5rem;
        border-radius: 50%;
        background-color: var(--primary-50);
      }

      .input-ingredient-name {
        padding: var(--spacing-03) 0;
        width: 60%;
      }

      .input-ingredient-quantity,
      .input-ingredient-quantity-ghost {
        position: relative;
        padding: var(--spacing-03) 0;
        padding-left: var(--spacing-04);
        width: 40%;

        &::before {
          content: '';
          position: absolute;
          top: var(--spacing-04);
          left: var(--spacing-02);
          height: 1em;
          display: inline-block;
          border-left: 1px solid var(--background-40);
        }

        ::v-deep input {
          text-align: right;
        }
      }

      .input-ingredient-quantity {
        display: none;
      }

      .input-ingredient-quantity-ghost {
        display: flex;
      }

      .units {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        padding: calc(var(--spacing-03) / 2);
        background-color: var(--background-20);

        li {
          margin: calc(var(--spacing-03) / 2);
        }

        input[type="radio"] {
          display: none;

          &:checked + label {
            color: var(--primary-60);
            background-color: var(--primary-40);
            box-shadow: none;

            i {
              color: var(--primary-50);
            }
          }
        }

        label {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          border-radius: 5px;
          color: var(--grey-70);
          background: var(--white);
          box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
          height: 2.5rem;
          padding: 0 var(--spacing-03);

          i {
            color: var(--background-50);
            height: 1.25em;
            width: 1.25em;
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
        }
      }

      .delete-ingredient,
      .units {
        width: 100%;
        display: none;
      }

      &.show-delete-button {
        .delete-ingredient {
          display: flex;
        }
      }

      &.show-units {
        .units,
        .input-ingredient-quantity {
          display: flex;
        }

        .input-ingredient-quantity-ghost {
          display: none;
        }
      }
    }

    .add-ingredient {
      display: flex;
      align-items: center;
      padding-top: var(--spacing-03);
      position: relative;
      width: calc(100% - 1.25rem - var(--spacing-02));
      margin-left: calc(1.25rem + var(--spacing-02));

      &::before {
        top: calc(1rem - 0.5rem / 2 - 2px + var(--spacing-03));
        background-color: var(--grey-30);
      }

      button {
        transition: background-color var(--speed-normal), border-color var(--speed-normal);
        border: dashed 2px;
        border-color: var(--background-40);

        &:hover,
        &:focus {
          border-color: var(--background-60);
        }
      }
    }
  }

  .steps {
    width: 100%;

    h2 {
      font-size: 0.875rem;
      font-weight: bold;
      text-transform: uppercase;
      text-align: center;
      color: var(--primary-50);
    }

    ol {
      list-style: none;
      counter-reset: li;
      margin-bottom: 0;
      padding: 0;
    }

    li {
      display: flex;
      align-items: center;
      position: relative;
      margin: var(--spacing-03) 0;
      line-height: 1.33em;
      padding-left: var(--spacing-04);
      background-color: var(--white);
      border-radius: 10px;
      box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
      transition: background-color var(--speed-normal);

      .textarea {
        padding-left: var(--spacing-06);
      }

      i {
        color: var(--background-40);
      }

      .textarea,
      i {
        opacity: 1;
        transition: opacity var(--speed-normal);
      }

      &.dragging {
        background: var(--background-30);

        .textarea,
        &::before {
          opacity: 0;
        }
      }
    }

    .add-step {
      transition: background-color var(--speed-normal), border-color var(--speed-normal);
      border: dashed 2px;
      border-color: var(--background-40);

      &:hover,
      &:focus {
        border-color: var(--background-60);
      }
    }
  }

  .actions {
    width: 100%;
    padding-top: var(--spacing-08);
  }
}
</style>
