import { TestBed } from '@angular/core/testing';

import { MetodosNumericosService } from './metodos-numericos.service';

describe('MetodosNumericosService', () => {
  let service: MetodosNumericosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MetodosNumericosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
