--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: motorsport; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.motorsport (
    nama character varying,
    harga bigint,
    cc real,
    kapasitas_bensin real,
    daya_maksimum real,
    torsi_maksimum real
);


ALTER TABLE public.motorsport OWNER TO postgres;

--
-- Data for Name: motorsport; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.motorsport (nama, harga, cc, kapasitas_bensin, daya_maksimum, torsi_maksimum) FROM stdin;
CB150X	33910000	149.16	12	11.5	13.8
CRF250L	79900000	249.67	7.8	18.9	23.1
CBR150R	37283000	149.16	12	12.6	14.4
CBR250RR	63456000	249.7	14.5	28.5	23.3
XSR 155	37775000	155	10.4	14.2	14.7
R15	39875000	155.09	11	14.2	14.7
R25	63450000	250	14	26.5	23.6
MT-25	57255000	155	14	26.5	23.6
MT-15	38525000	155	10.4	14.2	14.7
VIXION 155	29175000	155.1	12	12.2	14.7
\.


--
-- PostgreSQL database dump complete
--

