import { render, screen, fireEvent } from '@testing-library/react'
import '@testing-library/jest-dom'
import App from './App'

global.fetch = vi.fn().mockResolvedValue({ ok: true, json: async () => ({ message: 'Hello, Test!' }) }) as any

it('renders form and fetches greeting', async () => {
  render(<App />)
  const input = screen.getByLabelText(/name/i)
  fireEvent.change(input, { target: { value: 'Test' } })
  fireEvent.click(screen.getByRole('button', { name: /greet|saudar/i }))
  const result = await screen.findByText('Hello, Test!')
  expect(result).toBeInTheDocument()
})
