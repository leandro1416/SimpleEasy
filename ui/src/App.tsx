import { useEffect, useMemo, useState } from 'react'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000'

const i18n = {
  en: {
    title: 'SimpleEasy',
    name: 'Name',
    language: 'Language',
    timeGreet: 'Time-based greeting',
    submit: 'Greet',
    result: 'Result',
  },
  pt: {
    title: 'SimpleEasy',
    name: 'Nome',
    language: 'Idioma',
    timeGreet: 'Saudação por horário',
    submit: 'Saudar',
    result: 'Resultado',
  },
}

export default function App() {
  const [name, setName] = useState(localStorage.getItem('name') || '')
  const [lang, setLang] = useState<'en' | 'pt'>((localStorage.getItem('lang') as 'en' | 'pt') || 'en')
  const [time, setTime] = useState(localStorage.getItem('time') === 'true')
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const t = useMemo(() => i18n[lang], [lang])

  useEffect(() => {
    localStorage.setItem('name', name)
    localStorage.setItem('lang', lang)
    localStorage.setItem('time', String(time))
  }, [name, lang, time])

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault()
    if (!name.trim()) {
      setMessage('')
      return
    }
    setLoading(true)
    setMessage('')
    try {
      const url = new URL('/hello', API_BASE)
      url.searchParams.set('name', name.trim())
      url.searchParams.set('lang', lang)
      if (time) url.searchParams.set('time', 'true')
      const r = await fetch(url.toString())
      if (!r.ok) throw new Error(`HTTP ${r.status}`)
      const data = await r.json()
      setMessage(data.message || '')
    } catch (err: any) {
      setMessage(`Error: ${err.message || 'request failed'}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <header className="mx-auto max-w-2xl px-4 py-6">
        <h1 className="text-2xl font-semibold">{t.title}</h1>
      </header>
      <main className="mx-auto max-w-2xl px-4">
        <form onSubmit={onSubmit} className="space-y-4 bg-white p-4 rounded-lg shadow">
          <div>
            <label className="block text-sm font-medium mb-1" htmlFor="name">{t.name}</label>
            <input id="name" value={name} onChange={(e) => setName(e.target.value)}
              className="w-full rounded border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="Alice" />
          </div>
          <div className="flex items-center gap-4">
            <div className="flex-1">
              <label className="block text-sm font-medium mb-1" htmlFor="lang">{t.language}</label>
              <select id="lang" value={lang} onChange={(e) => setLang(e.target.value as 'en' | 'pt')}
                className="w-full rounded border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                <option value="en">English</option>
                <option value="pt">Português</option>
              </select>
            </div>
            <label className="inline-flex items-center space-x-2 mt-6">
              <input type="checkbox" checked={time} onChange={(e) => setTime(e.target.checked)} />
              <span className="text-sm">{t.timeGreet}</span>
            </label>
          </div>
          <button type="submit" disabled={loading}
            className="inline-flex items-center rounded bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700 disabled:opacity-60">
            {loading ? '…' : t.submit}
          </button>
        </form>

        <section className="mt-6">
          <h2 className="text-sm font-medium mb-2">{t.result}</h2>
          <div className="min-h-[3rem] rounded border border-dashed border-gray-300 p-3 bg-white">
            {message || <span className="text-gray-400">—</span>}
          </div>
        </section>

        <footer className="mt-8 text-sm text-gray-500">
          <a className="underline" href="http://127.0.0.1:8000/docs" target="_blank" rel="noreferrer">API docs</a>
        </footer>
      </main>
    </div>
  )
}
