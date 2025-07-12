from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from typing import List, Optional
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import io