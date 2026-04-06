from reportlab.pdfgen import canvas

c = canvas.Canvas('data/sample.pdf')
c.drawString(100, 750, 'What is Artificial Intelligence?')
c.drawString(100, 700, 'AI is the simulation of human intelligence by machines.')
c.drawString(100, 650, 'Machine learning is a subset of AI.')
c.drawString(100, 600, 'Deep learning uses neural networks with many layers.')
c.drawString(100, 550, 'Natural Language Processing helps computers understand text.')
c.drawString(100, 500, 'RAG stands for Retrieval Augmented Generation.')
c.drawString(100, 450, 'Vector databases store embeddings for fast similarity search.')
c.drawString(100, 400, 'LangChain is a framework for building LLM applications.')
c.save()
print('PDF created!')