const SITE_NAME = 'Lincoln Portfolio'
const DEFAULT_TITLE = 'Lincoln | Full-Stack Data Scientist'
const DEFAULT_DESCRIPTION =
  'Portfolio of Lincoln, a full-stack data scientist building AI systems, data tools, predictive analytics, and business-focused software.'
const SITE_URL = (import.meta.env.VITE_SITE_URL || window.location.origin).replace(/\/$/, '')

const upsertMeta = (selector, attributes) => {
  let element = document.head.querySelector(selector)

  if (!element) {
    element = document.createElement('meta')
    document.head.appendChild(element)
  }

  Object.entries(attributes).forEach(([key, value]) => {
    element.setAttribute(key, value)
  })
}

const upsertLink = (rel, href) => {
  let element = document.head.querySelector(`link[rel="${rel}"]`)

  if (!element) {
    element = document.createElement('link')
    element.setAttribute('rel', rel)
    document.head.appendChild(element)
  }

  element.setAttribute('href', href)
}

export const applySeo = (route) => {
  const title = route.meta?.title || DEFAULT_TITLE
  const description = route.meta?.description || DEFAULT_DESCRIPTION
  const canonicalUrl = new URL(route.path || '/', SITE_URL).toString()

  document.title = title

  upsertMeta('meta[name="description"]', { name: 'description', content: description })
  upsertMeta('meta[name="robots"]', {
    name: 'robots',
    content: route.meta?.noindex ? 'noindex, nofollow' : 'index, follow',
  })

  upsertMeta('meta[property="og:site_name"]', { property: 'og:site_name', content: SITE_NAME })
  upsertMeta('meta[property="og:type"]', { property: 'og:type', content: 'website' })
  upsertMeta('meta[property="og:title"]', { property: 'og:title', content: title })
  upsertMeta('meta[property="og:description"]', {
    property: 'og:description',
    content: description,
  })
  upsertMeta('meta[property="og:url"]', { property: 'og:url', content: canonicalUrl })

  upsertMeta('meta[name="twitter:card"]', { name: 'twitter:card', content: 'summary' })
  upsertMeta('meta[name="twitter:title"]', { name: 'twitter:title', content: title })
  upsertMeta('meta[name="twitter:description"]', {
    name: 'twitter:description',
    content: description,
  })

  upsertLink('canonical', canonicalUrl)
}
